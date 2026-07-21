import os
import shutil

source_folder = input("Enter folder path: ")

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        extension = file.split(".")[-1]

        folder = os.path.join(source_folder, extension.upper() + "_Files")

        if not os.path.exists(folder):
            os.makedirs(folder)

        shutil.move(file_path, os.path.join(folder, file))

print("Files organized successfully!")
