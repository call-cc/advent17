#!/usr/bin/env python3


import common


def captcha(num):
    sum = 0
    for i in range(-1, len(num) - 1):
        if num[i] == num[i + 1]:
            sum += int(num[i])

    return sum


if __name__ == '__main__':
    print(captcha(common.reader('input.txt')))
