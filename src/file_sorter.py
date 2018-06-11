import os

from src.file import File
from src.file_helper import FileHelper
from src.sort_type import SortType


class FileSorter:
    def __init__(self, folder_location, sort_type):
        self.folder_location = folder_location
        self.sort_type = sort_type

    def file_extensions(self):
        file_dict = dict()
        for real_file in os.listdir(self.folder_location):
            if os.path.isfile(os.path.join(self.folder_location, real_file)):
                file = File(real_file, self.folder_location, self.sort_type)
                try:
                    file_ext_array = file_dict[file.ext]
                except KeyError:
                    file_ext_array = []
                file_ext_array.append(file)
                file_dict[file.ext] = file_ext_array
        return file_dict

    def modification_dates(self):
        file_dict = dict()
        for real_file in os.listdir(self.folder_location):
            if os.path.isfile(os.path.join(self.folder_location, real_file)):
                file = File(real_file, self.folder_location, self.sort_type)
                try:
                    file_ext_array = file_dict[file.modification_date]
                except KeyError:
                    file_ext_array = []
                file_ext_array.append(file)
                file_dict[file.modification_date] = file_ext_array
        return file_dict

    def sort_files(self):
        """get sort type"""
        file_dict = None
        if self.sort_type == SortType.MODIFICATION_DATE:
            file_dict = self.modification_dates()
        elif self.sort_type == SortType.FILE_EXTENSION:
            file_dict = self.file_extensions()

        """create empty folder for each extension"""
        FileHelper.create_empty_folders(self.folder_location, file_dict.keys())

        """sort files into dirs"""
        for ext in file_dict.keys():
            for file in file_dict[ext]:
                os.rename(file.full_path, file.new_path)
