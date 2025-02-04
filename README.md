<p align = "center">
    <img src = "icons/pass.png" height = 150>
</p>

# Passlock Desktop 🗝️

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/AM-ash-OR-AM-I/PasslockDesktop)]

Passlock is a password manager that helps you store and manage your passwords securely. It uses AES encryption to store passwords in a local database file. It also has a feature to backup and sync your passwords to Firebase Realtime Database. It is a desktop version of the android app <a href="https://github.com/AM-ash-OR-AM-I/Passlock">Passlock</a>.

## Download 📥

[Download latest release 📥](https://github.com/AM-ash-OR-AM-I/PasslockDesktop/releases/latest)

<details>
<summary>Additional steps for linux</summary>

- Extract files to dir using `tar -xzvf passlock.tar.gz -C <output_path>`
- `cd passlock` & Just run `./install.sh` inside the passlock folder
  - It will ask for sudo password to create a softlink.
  - This will add a menu item and make passlock accessible through terminal anywhere
  - try `$ passlock` or run from menu.

#### Manually (In case script doesn't work)

<details>
<summary>Creating a soft link</summary>
After installing and extracting .tar.gz file in linux to run app anywhere in terminal we can create a softlink like this:

```$ ln -s /path/to/passlock/Passlock /usr/local/bin/passlock```

After this we can run passlock by typing `$ passlock`

</details>
<details>
<summary>Adding menu icon</summary>

```bash
cd ~/.local/share/applications
nano passlock.desktop
```

Paste the following lines by specifying the `/path/to/passlock` in `Exec` and `Icon` fields

```ini
[Desktop Entry]
Encoding=UTF-8
Version=1.3.0
Type=Application
Terminal=false
Exec=/path/to/passlock/Passlock
Name=Passlock
Icon=/path/to/passlock/pass.png
```

Now app can be launched from applications menu
</details>
</details>

### Issues

<details>
<summary>Linux</summary>

In linux you may face issues with app not starting, it's likely if `xrandr` isn't installed.

- Install `xrandr` by `$ sudo dnf xrandr` in fedora or `$ sudo apt xrandr` in ubuntu

</details>

<details>
<summary>MacOS</summary>

- In MacOS after installing app you may face issues with app not starting, it's likely due to quarantine attribute set by MacOS.

- Remove quarantine attribute by running the following command in terminal:

```bash
xattr -cr /path/to/Passlock.app
```

- Now you can run the app by double clicking on the app icon or optionally add it to dock.

</details>

## Setup 🛠️

- Clone repo `git clone https://github.com/AM-ash-OR-AM-I/PasslockDesktop.git` & `cd PasslockDesktop`
- Run the following command in terminal to install dependencies in a virtual environment.

```sh
pip install --upgrade pip
python -m venv env
env\Scripts\activate
python -m pip install -r requirements.txt
```

- Copy kivymd folder to site-packages
  - Windows: `xcopy kivymd\* env\Lib\site-packages\kivymd\ /E`
  - Linux/MacOS: `cp -r kivymd/ .</path/to/site-packages>/kivymd/`
- Make a file named `libs\firebase_config.py` with the following content:

```py
import os
os.environ["WEB_API_KEY"] = "[YOUR WEB API KEY HERE]" # Find web api key in firebase project settings
os.environ["DATABASE_URL"] = "[YOUR DATABASE URL HERE]" # Find database url in firebase project settings
```

- To sanity check if everything is working fine, run `python main.py` and see if the app runs.
- Also you can run `pip list` to see if only the packages in `requirements.txt` are installed.

## Packaging 📦

### Automated 🤖

- Run `.\build_windows.bat` to make windows build, optionally you can set version number by passing it as argument.
  - Example: `build_windows.bat 1.3.0`
  - This will first make .exe file using PyInstaller and then make MSI installer inside `Passlock-SetupFiles` folder.
- Run `./build_linux.bat` to make linux `.tar.gz` zip, optionally you can set version number by passing it as argument.

### Manually 🧑🏻‍💻 (In case automated build fails)

#### PyInstaller

- Run `copy_kv_files.py` to copy kv files to `all_files` folder that will be used by PyInstaller.
  - NOTE: Do this every time you make changes to kv files.
- Make sure environment is activated if not run `env\Scripts\activate` or `source env/bin/activate` for linux/darwin.
- Pyinstaller command to package app:
  - Windows `pyinstaller passlock_windows.spec --noconfirm`
  - Linux `pyinstaller passlock_linux.spec --noconfirm`
  - MacOS `pyinstaller passlock_macos.spec --noconfirm`
- Output will be in `dist/passlock` folder.

#### Advanced Installer (Windows only MSI Build)

- Download and install <a href="https://www.advancedinstaller.com/downloads.html">Advanced Installer</a>.
- Check to see if path is correct for advanced installer in `make_msi_build.bat` file.
- Run `make_msi_build.bat` to make MSI installer.
- Output will be in `Passlock-SetupFiles` folder.
- Run `Passlock-SetupFiles\Passlock.msi` to install and run app.
  - NOTE: While installing you should not install in `Program Files` or `Program Files (x86)` folder as it will not have write permissions and app will not be able to create database file. Install in `C:\Passlock` or `D:\Passlock` or any other drive.

## Screenshots 💻

| Welcome                              | Home                              |
|--------------------------------------|-----------------------------------|
| ![](./screenshots/WelcomeScreen.png) | ![](./screenshots/HomeScreen.png) |
| Create Strong Passwords              | Find                              |
| ![](./screenshots/DarkMode.png)      | ![](./screenshots/FindScreen.png) |
| Backup and Sync                      | Choose Different Colors           |
| ![](./screenshots/sync.png)          | ![](./screenshots/colors.png)     |

## Frameworks ⚙️

Made with 💖 in Python using <a href="https://github.com/kivy/kivy">Kivy</a> as framework, along with
<a href="https://github.com/kivymd/KivyMD">KivyMD</a> library.
