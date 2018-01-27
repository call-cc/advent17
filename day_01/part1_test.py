#!/usr/bin/env python3


import unittest
import part1
import common


class TestCaptcha(unittest.TestCase):
    def setUp(self):
        self.tests = [('example1.txt', 3),
                      ('example2.txt', 4),
                      ('example3.txt', 0),
                      ('example4.txt', 9),
                      ('input.txt', 1097)]

    def test_captcha(self):
        for filename, result in self.tests:
            num = common.reader(filename)
            self.assertEqual(part1.captcha(num), result)


if __name__ == '__main__':
    unittest.main()
