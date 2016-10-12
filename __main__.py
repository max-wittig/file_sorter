import os
import random


def main():
    print(location)
    #generate_random_files()
    sort_files()

def write_file(filename, content):
    with open(os.path.join(location, filename), "w") as f:
        f.write(content)


def get_file_extensions():
    file_dict = dict()
    for root, dirs, files in os.walk(location):
        for file in files:
            current_ext = file.split(".")[1]
            if current_ext not in file_ext:
                file_ext.append(current_ext)
    return file_ext


def sort_files():
    """create folder for each extension"""
    file_ext = get_file_extensions()
    for ext in file_ext:
        os.mkdir(os.path.join(location, ext))

    """sort files into dirs"""



def generate_random_files():
    num = 30
    ext = ["jpg", "txt", "json", "doc", "pdf"]
    for i in range(0, num):
        for e in ext:
            write_file(str(random.randint(0, 1000)) + "." + e, "Whatever")

if __name__ == '__main__':
    location = os.path.join(os.path.dirname(os.path.realpath(__file__)), "to_sort")
    main()