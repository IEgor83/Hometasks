"""parsing using bs4"""
import os
import uuid
import re
from time import sleep, time
import requests as req
import bs4 as bs
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from itertools import repeat
from src.maps.hash_map import HashMap


def timer_func(func):
    """Декоратор, замеряющий время выполнения функции"""

    def wrap_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        return result

    return wrap_func


def convert_to_word(string):
    """
    Функция конвертации строки в слова
    """
    for i in ".:;,«»°()":
        string = string.replace(i, " ")
    list_of_words = []
    for word in string.split():
        if word[0] in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"\
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            list_of_words.append(word)
        else:
            list_of_words.append(None)
    return list_of_words


def add_base_path(base_path):
    """Функция для создания родительской папки для функции wiki_parser"""
    if os.path.exists(base_path):
        print("Создание не удалось: папка base_path уже создана.\n", end="")
    else:
        os.mkdir(base_path)
        print("Папка base_path создана.\n", end="")


def from_list_to_file(lis, path):
    """Записать в файл список кортежей (key, value)"""
    with open(path, "w", encoding="utf-8") as file:
        for i in lis:
            print(i)
            file.write(f"{i[0]}\t{i[1]}\n")


def wiki_parser(url: str, base_path):
    """
    Функция для подсчета слов на странице википедии.
    """
    # Создание родительской папки.
    base_path += "\\base_path"
    add_base_path(base_path)

    # Проверка на наличия url в сохраненных файлах.
    flag = True
    dirlist = os.listdir(base_path)
    path = base_path  # путь до папки с файлами url.txt и content.bin
    for i in dirlist:
        with open(os.path.join(base_path, i, "url.txt"), "r", encoding="utf-8") as url_file:
            if url_file.read() == url:
                flag = False
                path = os.path.join(path, i)
                print("_____поиск url завершен, url уже был обработан_____\n", end="")
                break
    print("поиск url завершен, url еще не был обработан\n", end="")
    # Если url не нашелся, то создать папку с файлами url.txt, content.bin
    if flag:
        path = os.path.join(path, uuid.uuid4().hex)
        os.mkdir(path)
        with open(os.path.join(path, "url.txt"), "w", encoding="utf-8") as url_file:
            url_file.write(url)
        text = req.request("GET", url).content
        with open(os.path.join(path, "content.bin"), "wb") as content_file:
            content_file.write(text)

        print("_____url обработан_____\n", end="")
    # Подсчет слов с помощью HashMap. Сериализация HashMap в файл words.txt
    if not os.path.exists(os.path.join(path, "content.bin")):
        while True:
            sleep(0.1)
            if os.path.exists(os.path.join(path, "content.bin")):
                break
    with open(os.path.join(path, "content.bin"), "rb") as content_file:
        soup = bs.BeautifulSoup(content_file, "lxml")
        hash_map = HashMap()
        for string in soup.stripped_strings:
            for word in convert_to_word(string):
                if word is None:
                    continue
                try:
                    hash_map[word] += 1
                except KeyError:
                    hash_map[word] = 1
        from_list_to_file(sorted(hash_map.items(), key=lambda x: x[0]), os.path.join(path, "words.txt"))
        # Вернуть список всех ссылок на вики.
        href_list = []
        for tag in soup.find_all(href=re.compile("^/wiki/")):
            href_list.append("https://ru.wikipedia.org" + tag["href"])
        print("__________выполнение закончено__________\n", end="")
        return href_list


def merge(path1, path2, path):
    """
    Объединить два файла в один.
    """
    with open(path, "w", encoding="utf-8") as file:
        with open(path1, "r", encoding="utf-8") as file1:
            with open(path2, "r", encoding="utf-8") as file2:
                line_from_file1 = file1.readline()
                line_from_file2 = file2.readline()
                while True:
                    if line_from_file1 == "" and line_from_file2 == "":
                        break
                    if line_from_file1 == "":
                        while line_from_file2 != "":
                            file.write(line_from_file2)
                            line_from_file2 = file2.readline()
                        break
                    if line_from_file2 == "":
                        while line_from_file1 != "":
                            file.write(line_from_file1)
                            line_from_file1 = file1.readline()
                        break
                    if line_from_file1.split("\t")[0] < line_from_file2.split("\t")[0]:
                        file.write(line_from_file1)
                        line_from_file1 = file1.readline()
                    elif line_from_file1.split("\t")[0] > line_from_file2.split("\t")[0]:
                        file.write(line_from_file2)
                        line_from_file2 = file2.readline()
                    else:
                        temp1 = line_from_file1.split("\t")
                        temp2 = line_from_file2.split("\t")
                        file.write(temp1[0] + "\t" + str(int(temp1[1]) + int(temp2[1])) + "\n")
                        line_from_file1 = file1.readline()
                        line_from_file2 = file2.readline()


def multi_merge(paths, path):
    """
    Объединить файлы в один.
    """
    temp_path = path[:-4]
    paths_to_del = []
    while len(paths) > 2:
        curr_paths = []
        len_paths = len(paths)
        for i in range(0, len_paths - len_paths % 2, 2):
            temp = temp_path + uuid.uuid4().hex + ".txt"
            paths_to_del.append(temp)
            curr_paths.append(temp)
            merge(paths[i], paths[i + 1], temp)
        if len_paths % 2 == 1:
            curr_paths.append(paths[-1])
            paths = curr_paths
        else:
            paths = curr_paths
    merge(paths[0], paths[1], path)
    for i in paths_to_del:
        os.remove(i)


@timer_func
def multi(mode, url, base_path, max_workers=5, deep=3):
    """
    Функция, выполняющая функцию wiki_parser многопоточно или многопроцессорно.
    """
    beginning = wiki_parser(url, base_path)
    for _ in range(deep - 2):
        executor = mode(max_workers=max_workers)
        temp = []
        futures = [executor.submit(wiki_parser, url, path)
                   for url, path in zip(beginning, repeat(base_path))]
        for i in futures:
            temp += i.result()
        beginning = temp
        executor.shutdown()


#if __name__ == "__main__":
    #multi(ThreadPoolExecutor, 'https://ru.wikipedia.org/wiki/Бакаев,_Александр_Александрович',
          #r'C:\Users\Dell\PycharmProjects\Hometasks\src')
    #multi(ProcessPoolExecutor, 'https://ru.wikipedia.org/wiki/Бакаев,_Александр_Александрович',
          #r'C:\Users\Dell\PycharmProjects\Hometasks\src')


if __name__ == "__main__":
    wiki_parser('https://ru.wikipedia.org/wiki/Бакаев,_Александр_Александрович',
                r'C:\Users\Dell\PycharmProjects\Hometasks\src')
