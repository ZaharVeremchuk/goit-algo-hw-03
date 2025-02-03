import os
import shutil
import argparse

def copy_and_sort_files(source_dir, dest_dir):
    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)

            if os.path.isfile(source_path):
                # Якщо це файл, копіюємо його в відповідну папку
                ext = os.path.splitext(item)[1]
                if ext:
                    ext = ext[1:]  # Видаляємо крапку
                    dest_path = os.path.join(dest_dir, ext)
                    os.makedirs(dest_path, exist_ok=True)
                    shutil.copy2(source_path, os.path.join(dest_path, item))
            elif os.path.isdir(source_path):
                copy_and_sort_files(source_path, dest_dir)  # Передаємо той самий dest_dir
    except Exception as e:
        print(f"Помилка: {e}")

def main():
    parser = argparse.ArgumentParser(description="Сортує файли за розширенням.")
    parser.add_argument("source_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Шлях до директорії призначення")
    args = parser.parse_args()

    if not os.path.exists(args.source_dir):
        print(f"Помилка: Вихідна директорія '{args.source_dir}' не існує.")
        return

    try:
        os.makedirs(args.dest_dir, exist_ok=True) 
        copy_and_sort_files(args.source_dir, args.dest_dir)
        print("Сортування файлів завершено.")
    except Exception as e:
        print(f"Помилка: {e}")

# python homework1.py C:/Users/YourName/Documents/Source C:/Users/YourName/Documents/Destination
if __name__ == "__main__":
    main()
    