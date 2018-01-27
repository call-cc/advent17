import io
import sys


def reader(filename):
    with io.open(filename) as f:
        return f.readline().rstrip()
