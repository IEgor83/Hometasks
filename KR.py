class Number:
    def __init__(self, number=0):
        if number >= 0:
            self.number = [int(i) for i in str(number)]
        else:
            number = number*(-1)
            self.number = [int(i) for i in str(number)]
            self.number[0] = -self.number[0]

    def __add__(self, other):
        if self.number[0] < 0 or other.number[0] < 0:
            return self-(-other)
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
        def difference(a, b):
            r = len(a)-len(b)
            for i in range(len(a)-1, -1, -1):
                if (i-r) >= 0 and i > 0:
                    if a[i] < b[i-r]:
                        a[i - 1] -= 1
                    a[i] = (a[i] - b[i-r]) % 10
                elif i != 0:
                    if a[i] < 0:
                        a[i] = a[i] % 10
                        a[i - 1] -= 1
                    else:
                        break
                else:
                    if r == 0:
                        a[0] -= b[0]
                    for elem in a:
                        if elem == 0 and len(a) > 1:
                            a.pop(0)
                        else:
                            break
            return a
        if self >= other and self.number[0] > 0:
            if other.number[0] < 0:
                return self + (-other)
            new_obj = int(''.join(map(str, difference(self.number, other.number))))
        elif self < other and other.number[0] > 0:
            if self.number[0] < 0:
                return -(other-self)
            new_obj = -int(''.join(map(str, difference(other.number, self.number))))
        else:
            return (-other)-(-self)
        return Number(new_obj)

    def __neg__(self):
        new_obj = self.number.copy()
        new_obj[0] = -new_obj[0]
        new_object = int(''.join(map(str, new_obj)))
        return Number(new_object)

    def __eq__(self, other):
        if len(self.number) == len(other.number):
            for i in range(len(self.number)):
                if self.number[i] != other.number[i]:
                    return False
            return True
        return False

    def __lt__(self, other):
        if len(self.number) == len(other.number):
            for i in range(len(self.number)):
                if self.number[i] < other.number[i]:
                    return True
                if self.number[i] > other.number[i]:
                    return False
            return False
        return len(self.number) < len(other.number)

    def __le__(self, other):
        if len(self.number) == len(other.number):
            for i in range(len(self.number)):
                if self.number[i] < other.number[i]:
                    return True
                if self.number[i] > other.number[i]:
                    return False
            return True
        return len(self.number) < len(other.number)

    def __gt__(self, other):
        if len(self.number) == len(other.number):
            for i in range(len(self.number)):
                if self.number[i] > other.number[i]:
                    return True
                if self.number[i] < other.number[i]:
                    return False
            return False
        return len(self.number) > len(other.number)

    def __ge__(self, other):
        if len(self.number) == len(other.number):
            for i in range(len(self.number)):
                if self.number[i] > other.number[i]:
                    return True
                if self.number[i] < other.number[i]:
                    return False
            return True
        return len(self.number) > len(other.number)

    def __ne__(self, other):
        if len(self.number) == len(other.number):
            for i in range(len(self.number)):
                if self.number[i] != other.number[i]:
                    return True
            return False
        return True

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return repr(self.number)


s = Number(-135789)
p = Number(-37645231)
print(p-s)