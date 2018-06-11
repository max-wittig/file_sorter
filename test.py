import os
import tempfile
import unittest

from src.file_helper import FileHelper
from src.file_sorter import FileSorter
from src.sort_type import SortType


class FileSorterTests(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.FILES_PER_EXT = 30
        FileHelper.generate_random_files(self.test_dir.name, self.FILES_PER_EXT)

    def test_sort(self):
        file_sorter = FileSorter(self.test_dir.name, SortType.get_sort_type("fe"))
        file_sorter.sort_files()
        pdf_in_dir = len(os.listdir(os.path.join(self.test_dir.name, "pdf")))
        self.assertEqual(pdf_in_dir, self.FILES_PER_EXT)

    def test_file_extension_capitalized(self):
        file_sorter = FileSorter(self.test_dir.name, SortType.get_sort_type("fe"))
        file_sorter.sort_files()
        jpeg_in_dir = len(os.listdir(os.path.join(self.test_dir.name, "jpeg")))
        self.assertEqual(jpeg_in_dir, self.FILES_PER_EXT * 2)  # jpeg and JPEG should be treated the same

    def test_modification_date(self):
        file_sorter = FileSorter(self.test_dir.name, SortType.get_sort_type("md"))
        file_sorter.sort_files()
        pdf_in_dir = len(os.listdir(self.test_dir.name))
        self.assertEqual(pdf_in_dir, 1)  # file were all created on the same date

    def test_duplicate_files(self):
        file_sorter = FileSorter(self.test_dir.name, SortType.get_sort_type("fe"))
        file_name = "duplicate.txt"
        with open(os.path.join(self.test_dir.name, file_name), "w") as f:
            f.write("Duplicate")
        file_sorter.sort_files()
        with open(os.path.join(self.test_dir.name, file_name), "w") as f:
            f.write("Duplicate")
        file_sorter.sort_files()

    def tearDown(self):
        self.test_dir.cleanup()


if __name__ == '__main__':
    unittest.main()
