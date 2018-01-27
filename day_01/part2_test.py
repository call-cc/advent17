#!/usr/bin/env python3


import unittest
import part2
import common


class TestCaptcha(unittest.TestCase):
    def setUp(self):
        self.tests = [('example5.txt', 6),
                      ('example6.txt', 0),
                      ('example7.txt', 4),
                      ('example8.txt', 12),
                      ('example9.txt', 4),
                      ('input.txt', 1188)]

    def test_captcha(self):
        for filename, result in self.tests:
            num = common.reader(filename)
            self.assertEqual(part2.captcha(num), result)


if __name__ == '__main__':
    unittest.main()
