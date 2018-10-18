def read(path):
    with open(path) as f:
        return f.read()


def write(path, content, mode="w+"):
    with open(path, mode) as f:
        f.write(content)
