import os


class File:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_ext(self):
        return self.name.split(".")[1]

    def get_full_path(self):
        return os.path.join(self.location, self.name)

    def get_new_path(self):
        return os.path.join(self.location, self.get_ext(), self.name)
