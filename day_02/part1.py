#!/usr/bin/env python3


import common


def checksum(sheet):
    sum = 0
    for row in sheet:
        sum += max(row) - min(row)

    return sum


if __name__ == '__main__':
    print(checksum(common.reader('input.txt')))
