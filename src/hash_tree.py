
class NodeTree:
    def __init__(self, key: str = None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class HashTree:
    def __init__(self):
        self.head = None
        self.length = 0

    @classmethod
    def add(cls, a, key, value):
        if key > a.key:
            if a.right is None:
                a.right = NodeTree(key, value)
            else:
                cls.add(a.right, key, value)
        elif key < a.key:
            if a.left is None:
                a.left = NodeTree(key, value)
            else:
                cls.add(a.left, key, value)
        else:
            a.value = value

    def __setitem__(self, key, value):
        if self.head is None:
            self.head = NodeTree(key, value)
            self.length += 1
        else:
            a = self.head
            self.add(a, key, value)
            self.length += 1

    def __getitem__(self, key):
        a = self.head
        while a:
            if a.key == key:
                return a.value
            else:
                if key > a.key:
                    a = a.right
                else:
                    a = a.left
        raise KeyError

    def __delitem__(self, key):
        def del_elem(elem, key):
            if not elem:
                raise KeyError
            if elem.key > key:
                elem.left = del_elem(elem.left, key)
                return elem
            elif elem.key < key:
                elem.right = del_elem(elem.right, key)
                return  elem
            else:
                if elem.left and elem.right:
                    a = elem.left
                    while a.right:
                        a = a.right
                    elem.key = a.key
                    elem.value = a.value
                    elem.left = del_elem(elem.left, elem.key)
                    return elem
                elif elem.left:
                    return elem.left
                else:
                    return elem.right
        self.head = del_elem(self.head, key)
        self.length -= 1

    def __str__(self):
        def return_key(node):
            return f" {node.key}:{node.value} "

        def return_all(node):
            if node is None:
                return ''
            return return_all(node.left) + return_key(node) + return_all(node.right)

        return return_all(self.head)

    def __iter__(self):
        self.a = self
        return self

    def __next__(self):
        if self.length > 0:
            b = self.a.head
            while b.left:
                b = b.left
            del self.a[b.key]
            return b.key, b.value
        print(self.a)
        raise StopIteration


s = HashTree()
s[8] = 8
s[5] = 5
s[7] = 7
s[6] = 6
s[4] = 4
s[11] = 11
s[9] = 9
s[10] = 10
s[13] = 13
s[12] = 12

for i in s:
    print(i)
