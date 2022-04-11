import unittest

from random import randint

import src.hash_map as hm


class TestHashMap(unittest.TestCase):
    """ Tests of HashMap class methods """
    def test_init(self):
        """ We check that during initialization there will be an object
        of the LinkedList() class in each cell of the array """
        new_hm = hm.HashMap()
        for i in new_hm._inner_list:
            self.assertIsInstance(i, hm.LinkedList)

    def test_setitem(self):
        """ Test setitem """
        new_hm = hm.HashMap(1)
        new_hm['first'] = 'new_value'
        flag_check = True
        if not (new_hm._inner_list[hash('first') % new_hm._size].first.value is 'new_value'
            and new_hm._inner_list[hash('first') % new_hm._size].first.key is 'first'):
            flag_check = False
        new_hm['first'] = 'second_value'
        if not (new_hm._inner_list[hash('first') % new_hm._size].first.value is 'second_value'
            and new_hm._inner_list[hash('first') % new_hm._size].first.key is 'first'):
            flag_check = False
        self.assertIs(flag_check, True)
        self.assertEqual(new_hm._size, 2)
        self.assertEqual(new_hm._count, 1)

    def test_getitem(self):
        """ Test getitem """
        new_hm = hm.HashMap()
        for i in range(10):
            new_hm[i] = randint(1, 100)
        new_hm['check'] = 'value'
        val_check = new_hm['check']
        self.assertIs(val_check, 'value')
        flag = True
        try:
            print(new_hm['nothing'])
            flag = False
        except KeyError:
            self.assertIs(flag, True)

    def test_delitem(self):
        """ Test delitem """
        new_hm = hm.HashMap()
        for i in range(10):
            new_hm[i] = randint(1, 100)
        del new_hm[5]
        flag = True
        try:
            print(new_hm[5])
            flag = False
        except KeyError:
            self.assertIs(flag, True)


if __name__ == '__main__':
    unittest.main()