python ./utils/copy_kv_files.py
pyinstaller passlock_macos.spec --noconfirm
hdiutil create -volname "Passlock" -srcfolder "dist/Passlock.app" -ov -format UDZO "Passlock$1.dmg"
