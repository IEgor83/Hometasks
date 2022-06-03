from src.maps.base_map import BaseMap


class NodeTree:
    def __init__(self, key: str = None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class HashTree(BaseMap):
    def __init__(self):
        self.head = None
        self.length = 0

    def __setitem__(self, key, value):
        if self.head is None:
            self.head = NodeTree(key, value)
            self.length += 1
        else:
            def add(a, k, val):
                if k > a.key:
                    if a.right is None:
                        a.right = NodeTree(k, val)
                    else:
                        add(a.right, k, val)
                elif k < a.key:
                    if a.left is None:
                        a.left = NodeTree(k, val)
                    else:
                        add(a.left, k, val)
                else:
                    a.value = val
                    self.length -= 1
            add(self.head, key, value)
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
        def del_elem(elem, k):
            if not elem:
                raise KeyError
            if elem.key > k:
                elem.left = del_elem(elem.left, k)
                return elem
            elif elem.key < k:
                elem.right = del_elem(elem.right, k)
                return elem
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
            return "".join([return_all(node.left), return_key(node), return_all(node.right)])

        return return_all(self.head)

    def __iter__(self):
        def iteration(root):
            temp.append((root.key, root.value))
            if root.left:
                iteration(root.left)
            if root.right:
                iteration(root.right)
        temp = []
        iteration(self.head)
        return temp.__iter__()

    def __len__(self):
        return self.length


if __name__ == '__main__':
    s = HashTree()
    s[8] = 8
    s[5] = 5
    s[7] = 7
    s[8] = 6
    s[4] = 4
    s[11] = 11
    s[9] = 9
    s[10] = 10
    s[13] = 13
    s[12] = 12

    for i in s:
        print(i)
    print(s.head)
    print(s.length)
