class Node:
    """
    linked list node class
    """
    def __init__(self, value=None, next=None, key=None):
        self.value = value
        self.next = next
        self.key = key


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + '(' + str(current.key) + ')' + ','
            while current.next != None:
                current = current.next
                out += str(current.value) + '(' + str(current.key) + ')' + ','
            return out[:-1] + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, x, key):
        self.length += 1
        if self.first == None:
            self.last = self.first = Node(x, None, key)
        else:
            self.last.next = self.last = Node(x, None, key)


class HashMap:
    def __init__(self, _size=10):
        self._size = _size
        self._count = 0
        self._inner_list = [LinkedList() for i in range(self._size)]

    def __getitem__(self, key):
        c = self._inner_list[hash(key) % self._size].first
        while c:
            if c.key == key:
                return c.value
            c = c.next
        raise KeyError

    def __setitem__(self, key, x):
        a = self._inner_list[hash(key) % self._size].first
        y = 0
        while a:
            if a.key == key:
                a.value = x
                y = 1
                break
            a = a.next
        if y == 0:
            self._inner_list[hash(key) % self._size].add(x, key)
            self._count += 1
        if self._count >= 0.8 * self._size:
            self._size = self._size * 2
            a = [LinkedList() for i in range(self._size)]
            for i in self._inner_list:
                j = i.first
                while j:
                    a[hash(j.key) % self._size].add(j.value,j.key)
                    j = j.next
            self._inner_list = a

    def __delitem__(self, key):
        a = self._inner_list[hash(key) % self._size].first
        c = None
        while a:
            if a.key == key:
                if c != None:
                    c.next = a.next
                    a.next = None
                    self._inner_list[hash(key) % self._size].length -= 1
                    self._count -= 1
                else:
                    if a.next:
                        self._inner_list[hash(key) % self._size].first = a.next
                        a.next = None
                    self._inner_list[hash(key) % self._size].first = None
            a = a.next

    def __str__(self):
        out = ''
        for i in self._inner_list:
            out = out + str(i) + '\n'
        return out


