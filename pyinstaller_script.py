import os
excluded_modules = [
    'numpy',
    'jedi',
    'psutil',
    'tk',
    'ipython',
    'tcl',
    'tcl8',
    'tornado'
    ,'cv2'
]

append_string = ''
for mod in excluded_modules:
    append_string += f' --exclude-module {mod}'

# Run the shell command with all the exclude module parameters
os.system(f'pyinstaller --name Passlock --icon icon/pass_256.ico  main.py --noconfirm {append_string}')