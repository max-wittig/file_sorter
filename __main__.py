
import random
from file_sorter import *
from file_helper import *


def main():
    location = os.path.join(os.path.dirname(os.path.realpath(__file__)), "to_sort")
    file_sorter = FileSorter(location)
    file_sorter.sort_files()
    #file_sorter.file_helper.generate_random_files()

if __name__ == '__main__':
    main()
