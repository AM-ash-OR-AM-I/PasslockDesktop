python ./utils/copy_kv_files.py
pyinstaller passlock_linux.spec --noconfirm
cd dist && tar -czvf "passlock$1.tar.gz" passlock/*