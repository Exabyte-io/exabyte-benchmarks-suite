import importlib

import json


def read(path):
    with open(path, "rb") as f:
        # PROBLEM: Not all input file formats are utf-8
        # SOLUTION: Read bytes from file, then attempt to decode to string
        file_bytes = f.read()
        try:
            file_string = file_bytes.decode("utf-8")
            return file_string
        except UnicodeError:
            #print(f"Unable to decode file '{path}' - returning bytes")
            pass
        return file_bytes


def write(path, content, mode="w+"):
    # PROBLEM: Not all output file content is utf-8
    # SOLUTION: Encode string as bytes, then write bytes to file
    if type(content) == str:
        content = content.encode("utf-8")
    elif type(content) != bytes:
        raise TypeError()
    if "b" not in mode:
        mode = "b" + mode
    with open(path, mode) as f:
        f.write(content)


def get_class_by_reference(reference):
    """
    Returns property class for a given property name.

    Args:
        reference (str): class reference.

    Returns:

    """
    cls_name = reference.split('.')[-1]
    mod_name = '.'.join(reference.split('.')[:-1])
    return getattr(importlib.import_module(mod_name), cls_name)


def read_json(path):
    return json.loads(read(path))
