import importlib

import json


def read(path):
    with open(path) as f:
        return f.read()


def write(path, content, mode="w+"):
    with open(path, mode) as f:
        f.write(content)


def get_class_by_refernce(reference):
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
