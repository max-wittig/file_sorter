#!/usr/bin/python3
from file_sorter import *
from file_helper import *
import argparse


def get_args():
    parser = argparse.ArgumentParser("file_sorter")
    parser.add_argument("-d", "--directory", help="Which directory to sort")
    return vars(parser.parse_args())


def main():
    options = get_args()
    location = options["directory"]
    print(location)
    file_sorter = FileSorter(location)
    file_sorter.sort_files()
    #file_sorter.file_helper.generate_random_files()

if __name__ == '__main__':
    main()
