#!/usr/bin/env python3


import unittest

def hello(name):
    return f'Hello, {name}!'

def add(x, y):
    return x + y

class Test(unittest.TestCase):
    def test_hello(self):
        names = ['A', 'B', 'C', 'X', 'Y', 'Z']

        for name in names:
            self.assertEqual(hello(name), f'Hello, {name}!')

    def test_add(self):
        nums = {
            3: [1, 2],
            7: [3, 4],
            11: [5, 6]
        }

        for (k, v) in nums.items():
            self.assertEqual(add(v[0], v[1]), k)

if __name__ == '__main__':
    unittest.main()
