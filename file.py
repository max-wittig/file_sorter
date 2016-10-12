import os


class File:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_ext(self):
        file_and_ext = str(self.name).split(".")
        if type(file_and_ext) == list:
            file_and_ext.reverse()
            return file_and_ext[0]
        else:
            return " "

    def get_full_path(self):
        return os.path.join(self.location, self.name)

    def get_new_path(self):
        return os.path.join(self.location, self.get_ext(), self.name)
