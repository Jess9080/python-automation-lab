import os
import shutil

source_folder = "descargas"
files = os.listdir(source_folder)

for file in files:
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        extension = file.split(".")[-1].lower()
        target_folder = os.path.join(source_folder, extension)

        os.makedirs(target_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(target_folder, file))

print("Archivos organizados correctamente.")
