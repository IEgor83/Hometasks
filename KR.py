class Number:
    def __init__(self, number=0):
        if number >= 0:
            self.number = [int(i) for i in str(number)]
        else:
            number = number*(-1)
            self.number = [int(i) for i in str(number)]
            self.number[0] = -self.number[0]

    def __add__(self, other):
        if len(self.number) > len(other.number):
            max_mas = self.number
            min_mas = other.number
        else:
            min_mas = self.number
            max_mas = other.number
        r = len(max_mas)-len(min_mas)
        for i in range(len(max_mas)-1, -1, -1):
            if (i-r) >= 0 and i > 0:
                max_mas[i - 1] += (max_mas[i] + min_mas[i - r]) // 10
                max_mas[i] = (max_mas[i] + min_mas[i-r])%10
            elif i != 0:
                if max_mas[i] > 9:
                    max_mas[i] = max_mas[i] % 10
                    max_mas[i - 1] += 1
                else:
                    break
            else:
                if max_mas[i] > 9:
                    max_mas[i] = max_mas[i] % 10
                    max_mas.insert(0, 1)
            new_object = int(''.join(map(str, max_mas)))
        return Number(new_object)

    def __sub__(self, other):
        ...

    def __neg__(self):
        new_obj = self.number.copy()
        new_obj[0] = -new_obj[0]
        new_object = int(''.join(map(str, new_obj)))
        return Number(new_object)

    def __eq__(self, other):
        if len(self.number) == len(other.number):
            for i in range(len(self.number)):
                if self.number[0] != other.number[0]:
                    return False
            return True
        return False

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return repr(self.number)


s = Number(135789)
p = Number(37645231)
print(s == p)