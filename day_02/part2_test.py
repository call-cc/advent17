#!/usr/bin/env python3


import unittest
import part2
import common


class TestChecksum(unittest.TestCase):
    def setUp(self):
        self.tests = [('example2.txt', 9)]

    def test_checksum(self):
        for filename, result in self.tests:
            ssheet = common.reader(filename)
            self.assertEqual(part2.checksum(ssheet), result)


if __name__ == '__main__':
    unittest.main()
