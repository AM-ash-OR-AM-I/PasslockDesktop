import os
import platform

my_files = os.walk("libs")
kivymd_files = os.walk("kivymd")
os.makedirs("all_files", exist_ok=True)


def copy_kv_files(my_files):
    for path, _, file_list in my_files:
        for file_name in file_list:
            if (
                file_name.endswith(".kv")
                or file_name.endswith(".png")
                or file_name.endswith(".ttf")
            ):
                dir_name = os.path.join("all_files", path)
                os.makedirs(dir_name, exist_ok=True)
                file_path = os.path.join(path, file_name)
                if platform.system() == "Windows":
                    os.system(f"copy {file_path} {dir_name}")
                else:
                    os.system(f"cp {file_path} {dir_name}")


if __name__ == "__main__":
    copy_kv_files(my_files)
    copy_kv_files(kivymd_files)
