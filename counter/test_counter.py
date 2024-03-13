"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
from counter import Counter
import unittest


class CounterTest(unittest.TestCase):
    def setUp(self):
        self.x = Counter()
        self.y = Counter()

    def test_singleton(self):
        self.x.increment()
        self.assertEqual(self.x, self.y)

    def test_both_increase(self):
        self.x.increment()
        self.y.increment()
        self.assertEqual(self.x, self.y)

    def test_edge_case(self):
        a = Counter()
        a.increment()
        b = Counter()
        print(a.count)
        print(b.count)
        self.assertEqual(a,b)