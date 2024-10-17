import os
import shutil

def copy_and_sort_files(source_dir, dest_dir):
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)

        if os.path.isfile(source_path):
            # Якщо це файл, копіюємо його в відповідну папку
            ext = os.path.splitext(item)[1]
            dest_path = os.path.join(dest_dir, ext[1:])
            os.makedirs(dest_path, exist_ok=True)
            shutil.copy2(source_path, dest_path)
        elif os.path.isdir(source_path):
            # Якщо це папка, рекурсивно викликаємо функцію для цієї папки
            new_dest = os.path.join(dest_dir, item)
            os.makedirs(new_dest, exist_ok=True)
            copy_and_sort_files(source_path, new_dest)
            
source_folder = "C:/Users/YourName/Documents/Source"
destination_folder = "C:/Users/YourName/Documents/Destination"
copy_and_sort_files(source_folder, destination_folder)