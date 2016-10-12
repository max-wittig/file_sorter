import os
from file_helper import *
from file import *


class FileSorter:
    def __init__(self, folder_location):
        self.folder_location = folder_location
        self.file_helper = FileHelper(folder_location)

    def get_file_extensions(self):
        file_dict = dict()
        for real_file in os.listdir(self.folder_location):
            if os.path.isfile(os.path.join(self.folder_location, real_file)):
                file = File(real_file, self.folder_location)
                try:
                    file_ext_array = file_dict[file.get_ext()]
                except KeyError:
                    file_ext_array = []
                file_ext_array.append(file)
                file_dict[file.get_ext()] = file_ext_array
        return file_dict

    def sort_files(self):
        """create empty folder for each extension"""
        file_dict = self.get_file_extensions()
        self.file_helper.create_empty_folders(file_dict.keys())

        """sort files into dirs"""
        for ext in file_dict.keys():
            for file in file_dict[ext]:
                os.rename(file.get_full_path(), file.get_new_path())
