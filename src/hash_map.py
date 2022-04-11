class Node:
    """ linked list node class """
    def __init__(self, value=None, next=None, key=None):
        self.value = value
        self.next = next
        self.key = key


class LinkedList:
    """ linked list class """
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + '(' + str(current.key) + ')' + ','
            while current.next is not None:
                current = current.next
                out += str(current.value) + '(' + str(current.key) + ')' + ','
            return out[:-1] + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, elem, key):
        self.length += 1
        if self.first is None:
            self.last = self.first = Node(elem, None, key)
        else:
            self.last.next = self.last = Node(elem, None, key)

    def __iter__(self):
        self.a = self.first
        return self

    def __next__(self):
        if self.a is None:
            raise StopIteration
        else:
            elem = self.a.value
            self.a = self.a.next
            return elem


class HashMap:
    """ HashMap class """
    def __init__(self, _size=10):
        self._size = _size
        self._count = 0
        self._inner_list = [LinkedList() for i in range(self._size)]

    def __getitem__(self, key):
        list_elem = self._inner_list[hash(key) % self._size].first
        while list_elem:
            if list_elem.key == key:
                return list_elem.value
            list_elem = list_elem.next
        raise KeyError

    def __setitem__(self, key, var):
        list_elem = self._inner_list[hash(key) % self._size].first
        flag = False
        while list_elem:
            if list_elem.key == key:
                list_elem.value = var
                flag = True
                break
            list_elem = list_elem.next
        if not flag:
            self._inner_list[hash(key) % self._size].add(var, key)
            self._count += 1
        if self._count >= 0.8 * self._size:
            self._size = self._size * 2
            list_elem = [LinkedList() for i in range(self._size)]
            for i in self._inner_list:
                j = i.first
                while j:
                    list_elem[hash(j.key) % self._size].add(j.value, j.key)
                    j = j.next
            self._inner_list = list_elem

    def __delitem__(self, key):
        elem = self._inner_list[hash(key) % self._size].first
        prev_elem = None
        flag = False
        while elem:
            if elem.key == key:
                flag = True
                if prev_elem is not None:
                    prev_elem.next = prev_elem.next
                    elem = None
                else:
                    if elem.next:
                        self._inner_list[hash(key) % self._size].first = elem.next
                        elem = None
                    else:
                        self._inner_list[hash(key) % self._size].first = None
                        self._inner_list[hash(key) % self._size].last = None
                self._inner_list[hash(key) % self._size].length -= 1
                self._count -= 1
                break
            prev_elem = elem
            elem = elem.next
            self._inner_list[hash(key) % self._size].first.next = prev_elem.next
        if not flag:
            raise KeyError

    def __str__(self):
        out = ''
        for i in self._inner_list:
            out = out + str(i) + '\n'
        return out

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == len(self._inner_list):
            raise StopIteration
        else:
            return self._inner_list[self.counter]


s = HashMap(6)
s[1] = 4
s[3] = 5
s[5] = 0
for i in s:
    print(i)
