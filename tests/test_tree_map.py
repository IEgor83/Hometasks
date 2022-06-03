import unittest

from random import shuffle

import src.maps.tree_map as ht


class TestHashMap(unittest.TestCase):
    """ Tests of HashMap class methods """

    def test_setitem(self):
        """ Test setitem """
        new_ht = ht.HashTree()
        new_ht[6] = 'six'
        new_ht[4] = 'four'
        new_ht[5] = 'five'
        new_ht[3] = 'three'
        new_ht[9] = 'nine'
        new_ht[7] = 'seven'
        new_ht[8] = 'eight'
        flag_check = True
        if not (new_ht.head.left.right.key is 5 and new_ht.head.left.right.value is 'five'):
            flag_check = False
        new_ht[5] = 'second_five'
        if not (new_ht.head.left.right.key is 5 and new_ht.head.left.right.value is 'second_five'):
            flag_check = False
        self.assertIs(flag_check, True)
        self.assertEqual(new_ht.length, 7)

    def test_getitem(self):
        """ Test getitem """
        new_ht = ht.HashTree()
        list_of_num = list(range(1, 15))
        shuffle(list_of_num)
        for i in list_of_num:
            new_ht[i] = i+1
        val_check = new_ht[9]
        self.assertIs(val_check, 10)
        flag = True
        try:
            print(new_ht[20])
            flag = False
        except KeyError:
            self.assertIs(flag, True)


if __name__ == '__main__':
    unittest.main()
