import unittest
from find_long_substr import *

class TestFindLongSubStr(unittest.TestCase):

    def setUp(self):
        self.mock = [
            {
                'i': 'abcabcbb',
                'o': 3,
            },{
                'i': 'bbbbb',
                'o': 1,
            },{
                'i': 'pwwkew',
                'o': 3,
            },
        ]


    def test_find_long_substr(self):
        for i in self.mock:
            self.assertEqual(find_long_substr_len(i.get('i')), i.get('o'))


