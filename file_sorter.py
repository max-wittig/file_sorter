import os
from sort_type import *
from file_helper import *
from file import *


class FileSorter:
    def __init__(self, folder_location, sort_type):
        self.folder_location = folder_location
        self.sort_type = sort_type
        self.file_helper = FileHelper(folder_location)

    def get_file_extensions(self):
        file_dict = dict()
        for real_file in os.listdir(self.folder_location):
            if os.path.isfile(os.path.join(self.folder_location, real_file)):
                file = File(real_file, self.folder_location, self.sort_type)
                try:
                    file_ext_array = file_dict[file.get_ext()]
                except KeyError:
                    file_ext_array = []
                file_ext_array.append(file)
                file_dict[file.get_ext()] = file_ext_array
        return file_dict

    def get_modification_date(self):
        file_dict = dict()
        for real_file in os.listdir(self.folder_location):
            if os.path.isfile(os.path.join(self.folder_location, real_file)):
                file = File(real_file, self.folder_location, self.sort_type)
                try:
                    file_ext_array = file_dict[file.get_modification_date()]
                except KeyError:
                    file_ext_array = []
                file_ext_array.append(file)
                file_dict[file.get_modification_date()] = file_ext_array
        return file_dict

    def sort_files(self):
        """get sort type"""
        file_dict = None
        if self.sort_type == SortType.MODIFICATION_DATE:
            file_dict = self.get_modification_date()
        elif self.sort_type == SortType.FILE_EXTENSION:
            file_dict = self.get_file_extensions()

        """create empty folder for each extension"""
        self.file_helper.create_empty_folders(file_dict.keys())

        """sort files into dirs"""
        for ext in file_dict.keys():
            for file in file_dict[ext]:
                os.rename(file.get_full_path(), file.get_new_path())
