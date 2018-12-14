#!/usr/bin/python
import os

def mkdir(directory):
    """
    Creates a directory if it doesn't already exist

    Args:
        directory (str): the full pathname of the directory to be created if not already available
    """
    if not os.path.exists(directory):
        os.mkdir(directory)


def replace_variables(dictionary, filename):
    """
    Does variable replacement within a file by reading the file into memory

    Args:
        dictionary (dict): dictionary of the keys and their replacements
        filename (str): name of file to be operated on
    """
    with open(filename, 'r') as file:
        filedata = file.read()
    file.close()
    filedata = filedata.format(**dictionary)
    with open(filename, 'w') as file:
        file.write(filedata)
    file.close()


def read_file_lines(filename):
    """
    Reads file by line and returns an array the file into memory

    Args:
        filename (str): name of file to be operated on
    """
    with open(filename) as temp_file:
        file_as_array = [line.rstrip('\n') for line in temp_file]
    return file_as_array


def is_valid_file(parser, arg):
    """
    Checks to make sure the arguments supplied exist as a real path

    Args:
        parser (obj): object to parse input arguments
        arg (str): pathname to a directory
    """
    if not os.path.exists(arg):
        parser.error("The directory %s does not exist!" % arg)
        return
    else:
        return arg  # return the path name
