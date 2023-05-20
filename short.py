#!/usr/bin/env python3


import unittest

hello = lambda n: f'Hello, {n}!'
add = lambda x, y: x + y

class Test(unittest.TestCase):
    def test_hello(self):
        n = ['A', 'B', 'C', 'X', 'Y', 'Z']
        [self.assertEqual(hello(i), f'Hello, {i}!') for i in n]

    def test_add(self):
        n = { 3: [1, 2], 7: [3, 4], 11: [5, 6] }
        [self.assertEqual(add(v[0], v[1]), k) for (k, v) in n.items()]

if __name__ == '__main__':
    unittest.main()
