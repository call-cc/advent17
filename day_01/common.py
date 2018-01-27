import io


def reader(filename):
    with io.open(filename) as f:
        return f.readline().rstrip()
