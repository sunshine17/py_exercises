import unittest
from spiral_matrix import spiral_order

class TestSpiralOrder(unittest.TestCase):

    def setUp(self):
        self.mock = [{
            'i': [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],
            'o': [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13],
        },]

    def test_spiral_order(self):
        for i in self.mock:
            self.assertEqual(spiral_order(i.get('i')), i.get('o'))