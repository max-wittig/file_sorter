import os
import uuid


class FileHelper:
    @staticmethod
    def create_empty_folders(folder_location, folder_names):
        for ext in folder_names:
            if not ext:
                ext = "none"
            path = os.path.join(folder_location, ext)
            if not os.path.exists(path):
                os.mkdir(path)

    @staticmethod
    def generate_random_files(folder_location, num_per_ext):
        ext = ["jpg", "txt", "json", "doc", "pdf",
               "", "exe", "bin", "JPEG", "jpeg"]
        for i in range(0, num_per_ext):
            for e in ext:
                file_name = str(uuid.uuid4()) + "." + e
                with open(os.path.join(folder_location, file_name), "w") as f:
                    f.write("Testing")
