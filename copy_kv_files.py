import os

files = os.walk("libs")
os.makedirs("all_files", exist_ok=True)
for path, dir_list, file_list in files:
    for file_name in file_list:
        if file_name.endswith(".kv"):
            file_path = os.path.join(path, file_name)
            os.makedirs(f"all_files\{path}", exist_ok=True)
            os.system(f"copy {file_path} all_files\{path}")
