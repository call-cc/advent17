#!/usr/bin/env python3


import common


def captcha(num):
    sum = 0
    l = len(num)
    for i in range(-1, l - 1):
        if num[i] == num[(i + l // 2) % l]:
            sum += int(num[i])

    return sum


if __name__ == '__main__':
    print(captcha(common.reader('input.txt')))
