from enum import Enum


class SortType(Enum):
    FILE_EXTENSION = 1
    MODIFICATION_DATE = 2

    @staticmethod
    def get_sort_type(sort_type_string):
        if sort_type_string == "fe":
            return SortType.FILE_EXTENSION
        elif sort_type_string == "md":
            return SortType.MODIFICATION_DATE
