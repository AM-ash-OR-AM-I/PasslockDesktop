@ECHO OFF
IF "%1"=="" (set version=1.0.0) ELSE (set version=%1)
echo "Version: %version%"
python utils\copy_kv_files.py
env\Scripts\activate && pyinstaller passlock_windows.spec --noconfirm && .\make_msi_build.bat %version%