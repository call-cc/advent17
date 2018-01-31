#!/usr/bin/env python3


import unittest
import common


class TestCommon(unittest.TestCase):
    def setUp(self):
        self.tests = [('example1.txt', [[5, 1, 9, 5],
                                        [7, 5, 3],
                                        [2, 4, 6, 8]]),
                      ('example2.txt', [[5, 9, 2, 8],
                                        [9, 4, 7, 3],
                                        [3, 8, 6, 5]])]

    def test_reader(self):
        for filename, result in self.tests:
            ssheet = common.reader(filename)
            self.assertEqual(ssheet, result)


if __name__ == '__main__':
    unittest.main()
