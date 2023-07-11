import os
import platform

my_files = os.walk("libs")
os.makedirs("all_files", exist_ok=True)
extensions = (".kv", ".png", ".ttf", ".atlas")

def copy_kv_files():
    for path, _, file_list in my_files:
        for file_name in file_list:
            if not file_name.endswith(extensions):
                continue
            dir_name = os.path.join("all_files", path)
            os.makedirs(dir_name, exist_ok=True)
            file_path = os.path.join(path, file_name)
            if platform.system() == "Windows":
                os.system(f"copy {file_path} {dir_name}")
            else:
                os.system(f"cp {file_path} {dir_name}")

copy_kv_files()