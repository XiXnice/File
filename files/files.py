from hashlib import new
import os

def compile_files(files_list):
    data = {}
    for file in files_list:
        with open(file, encoding="utf-8") as f:
            file_data = f.readlines()
            data[len(file_data)] = (file, "".join(file_data))

    data = dict(sorted(data.items()))

    with open("files/work.txt", "w", encoding="utf-8") as new_file:
        for key, value in data.items():
            # new_file.write(f"{value[0]} \n")
            new_file.write(f"{key} \n")
            new_file.write(f"{value[1]} \n")

files = ["files/1.txt", "files/2.txt", "files/3.txt"]
files = [os.path.join(os.getcwd(), file) for file in files]
compile_files(files)
