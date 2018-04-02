import os
import datetime
from sort_type import *
import uuid
from pathlib import Path


class File:
    def __init__(self, name, location, sort_type):
        self.name = name
        self.location = location
        self.sort_type = sort_type
        self.date_format = '%d-%m-%Y'

    @property
    def modification_date(self):
        t = os.path.getmtime(self.full_path)
        return datetime.date.fromtimestamp(t).strftime(self.date_format)

    @property
    def ext(self):
        file_and_ext = str(self.name).split(".")
        if type(file_and_ext) == list and len(file_and_ext) > 1:
            file_and_ext.reverse()
            return str(file_and_ext[0]).lower()
        else:
            return "none"

    @property
    def full_path(self):
        return os.path.join(self.location, self.name)

    @property
    def base_name(self):
        return Path(self.name).resolve().stem

    @property
    def new_path(self):
        new_name = self.name
        if self.sort_type == SortType.FILE_EXTENSION:
            if self.name in os.listdir(os.path.join(self.location, self.ext)):
                new_name = self.base_name + "-" + str(uuid.uuid4())[:5] + "." + self.ext
            return os.path.join(self.location, self.ext, new_name)
        elif self.sort_type == SortType.MODIFICATION_DATE:
            if self.name in os.listdir(os.path.join(self.location, self.modification_date)):
                new_name = self.base_name + "-" + str(uuid.uuid4())[:5] + "." + self.ext
            return os.path.join(self.location, self.modification_date, new_name)
