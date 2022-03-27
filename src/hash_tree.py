class NodeTree:
    def __init__(self, key = None, value = None, left = None, right = None):
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
        if self.head == None:
            self.head = NodeTree(key,value)
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
        return None

    def __delitem__(self, key):
        def del_elem(elem,key):
            if elem.key == key:
                if elem.left:
                    a = elem.left
                    while a.right:
                        if a.right.right == None:
                            break
                        a = a.right
                    if a.right:
                        a.right.right = elem.right
                        a.right.left,a.right = elem.left,a.right.left
                    else:
                        a.right = elem.right
                    return a
                elif elem.right:
                    return elem.right
                else:
                    return None
            else:
                if elem.key > key:
                    elem.left = del_elem(elem.left, key)
                    return elem
                else:
                    elem.right = del_elem(elem.right, key)
                    return elem
        self.head = del_elem(self.head,key)







