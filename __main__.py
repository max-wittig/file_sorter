#!/usr/bin/python3
from file_sorter import *
from file_helper import *
from sort_type import *
import argparse


def get_args():
    parser = argparse.ArgumentParser("file_sorter")
    parser.add_argument("-d", "--directory", help="Which directory to sort", required=True)
    parser.add_argument("-s", "--sort-type",
                        help="What to sort --> fe = file_extension || md == modification_date", default="fe")
    return vars(parser.parse_args())


def main():
    options = get_args()
    sort_type = SortType.get_sort_type(options["sort_type"])
    location = options["directory"]
    file_sorter = FileSorter(location, sort_type)
    file_sorter.sort_files()
    #file_sorter.file_helper.generate_random_files()

if __name__ == '__main__':
    main()
