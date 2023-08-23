# Soft-link for global access
sudo ln -s "$(pwd)/Passlock" /usr/local/bin/passlock

# Create Desktop Entry
echo "[Desktop Entry]
Encoding=UTF-8
Version=1.3.0
Type=Application
Terminal=false
Exec=$(pwd)/Passlock
Name=Passlock
Icon=$(pwd)/pass.png" > ~/.local/share/applications/passlock.desktop