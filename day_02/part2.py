#!/usr/bin/env python3


import common


def divide(a, b):
    if b > a:
        a, b = b, a

    return 0 if a % b else a // b


def worker(first, row):
    res = 0
    for i in row:
        res = divide(first, i)
        if res != 0:
            return res

    return worker(row[0], row[1:])


def checksum_row(row):
    return worker(row[0], row[1:])


def checksum(sheet):
    csum = 0
    for row in sheet:
        csum += checksum_row(row)

    return csum


if __name__ == '__main__':
    print(checksum(common.reader('input.txt')))
