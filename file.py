import os
import datetime
from sort_type import *


class File:
    def __init__(self, name, location, sort_type):
        self.name = name
        self.location = location
        self.sort_type = sort_type
        self.date_format = '%d-%m-%Y'

    def get_modification_date(self):
        t = os.path.getmtime(self.get_full_path())
        return datetime.date.fromtimestamp(t).strftime(self.date_format)

    def get_ext(self):
        file_and_ext = str(self.name).split(".")
        if type(file_and_ext) == list and len(file_and_ext) > 1:
            file_and_ext.reverse()
            return str(file_and_ext[0]).lower()
        else:
            return "none"

    def get_full_path(self):
        return os.path.join(self.location, self.name)

    def get_new_path(self):
        if self.sort_type == SortType.FILE_EXTENSION:
            return os.path.join(self.location, self.get_ext(), self.name)
        elif self.sort_type == SortType.MODIFICATION_DATE:
            return os.path.join(self.location, self.get_modification_date(), self.name)