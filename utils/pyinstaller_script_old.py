import os

excluded_modules = [
    "numpy",
    "jedi",
    "psutil",
    "tk",
    "ipython",
    "tcl",
    "tcl8",
    "tornado",
    "cv2",
]

append_string = ""
for mod in excluded_modules:
    append_string += f" --exclude-module {mod}"

datas_list = [
    ("all_files/", "."),
    ("fonts/", "fonts/"),
    ("icons/pass.png", "."),
    ("api_key.txt", "."),
]

add_datas = "".join([f"--add-data {data[0]}{os.pathsep}{data[1]} " for data in datas_list])
# Run the shell command with all the exclude module parameters


"""
Run this script to copy all .kv files in linux:

find libs/ -name "*.kv" | cpio -pdm all_files/

"""
os.system(f"pyinstaller --name Passlock_no_dep --icon icons/pass_256.ico {add_datas} main.py --noconfirm {append_string}")
# os.system(
#     f"pyinstaller --name Passlock_no_dep --icon icons/pass_256.ico --add-data  main.py --noconfirm {append_string}"
# )
