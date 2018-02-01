#!/usr/bin/env python3


import unittest
import part2
import common


class TestChecksum(unittest.TestCase):
    def testDivide(self):
        tests = [(1, 2, 2),
                 (2, 1, 2),
                 (2, 8, 4),
                 (8, 2, 4),
                 (5, 2, 0),
                 (2, 5, 0),
                 (9999, 33, 303)]

        for a, b, result in tests:
            self.assertEqual(part2.divide(a, b), result)

    def testWorker(self):
        tests = [([5, 9, 2, 8], 4),
                 ([2, 5, 9, 8], 4),
                 ([9, 4, 7, 3], 3),
                 ([9, 3, 4, 7], 3),
                 ([3, 8, 6, 5], 2),
                 ([8, 3, 6, 5], 2)]

        for row, result in tests:
            self.assertEqual(part2.worker(row[0], row[1:]), result)

    def test_checksum(self):
        self.tests = [('example2.txt', 9),
                      ('input.txt', 258)]

        for filename, result in self.tests:
            ssheet = common.reader(filename)
            self.assertEqual(part2.checksum(ssheet), result)


if __name__ == '__main__':
    unittest.main()
