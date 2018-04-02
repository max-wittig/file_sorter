import os
import random


class FileHelper:
    def __init__(self, folder_location):
        self.folder_location = folder_location

    def write_file(self, filename, content):
        with open(os.path.join(self.folder_location, filename), "w") as f:
            f.write(content)

    def create_empty_folders(self, folder_names):
        for ext in folder_names:
            path = os.path.join(self.folder_location, ext)
            if not os.path.exists(path):
                os.mkdir(path)

    def generate_random_files(self):
        num = 30
        ext = ["jpg", "txt", "json", "doc", "pdf"]
        for i in range(0, num):
            for e in ext:
                self.write_file(str(random.randint(0, 1000)) + "." + e, "Whatever")
