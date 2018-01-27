#!/usr/bin/env python3


import unittest
import part1
import common


class TestChecksum(unittest.TestCase):
    def setUp(self):
        self.tests = [('example1.txt', 18),
                      ('example2.txt', 18),
                      ('input.txt', 39126)]

    def test_checksum(self):
        for filename, result in self.tests:
            ssheet = common.reader(filename)
            self.assertEqual(part1.checksum(ssheet), result)


if __name__ == '__main__':
    unittest.main()
