import io
import re


def reader(filename):
    ssheet = []
    with io.open(filename) as f:
        for line in f.readlines():
            row = re.split(r'[ \t]', line.rstrip())
            ssheet.append(list(map(int, row)))

    return ssheet
