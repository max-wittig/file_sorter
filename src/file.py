import datetime
import hashlib
import os
from pathlib import Path

from src.sort_type import SortType


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
        return Path(self.name).suffix.lower().replace(".", "")

    @property
    def full_path(self):
        return os.path.join(self.location, self.name)

    @property
    def base_name(self):
        return Path(self.name).stem

    @property
    def hash(self):
        hash_md5 = hashlib.md5()
        if os.path.exists(self.name):
            with open(self.name, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @property
    def new_path(self):
        new_name = self.name
        folder_name = ""
        if self.sort_type == SortType.FILE_EXTENSION:
            folder_name = self.ext if self.ext else "none"
        elif self.sort_type == SortType.MODIFICATION_DATE:
            folder_name = self.modification_date

        if self.name in os.listdir(os.path.join(self.location, folder_name)):
            new_name = self.base_name + self.hash[:5] + "." + folder_name
        return os.path.join(self.location, folder_name, new_name)
