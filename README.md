<p align = "center">
    <img src = "icons/pass.png" height = 150>
</p>
<h3>Passlock (PC) - A powerful cross-platform password manager.</h3>


## Features 🌟
* Backup and sync passwords across devices 💻📱.
* Encrypted passwords using AES 128bit for maximum security.
* Mimics Material v3 Monet engine with 🌙 Dark Mode, to use different 🎨 color themes. (Self-made)
* Make strong passwords 🔑 through built in password generator.
* Advanced 🔍 finding algorithm to search for passwords easily.

## Releases 🚀
#### 🧑🏻‍💻<a href="https://github.com/AM-ash-OR-AM-I/PasslockDesktop/releases">Linux & Windows</a>
#### <a href="https://github.com/AM-ash-OR-AM-I/Passlock">📱Android</a>

### Additional (optional) steps for linux 
<details>
<summary><h4>Creating a soft link</h4></summary>
After installing and extracting .tar.gz file in linux to run app anywhere in terminal we can create a softlink like this:

```$ ln -s /path/to/passlock/Passlock /usr/local/bin/passlock```

After this we can run passlock by typing `$ passlock`

</details>
<details>
<summary><h4>Adding menu icon</h4></summary>
Hello there, if you are using linux and want to add passlock to applications menu then follow these steps:

```bash
$ cd ~/.local/share/applications
$ nano passlock.desktop
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


## Installation 📥
- Run the following command in terminal to install dependencies in a virtual environment.
```sh
pip install --updgrade pip
python -m venv env
env\Scripts\activate
python -m pip install -r requirements.txt
```
- Copy kivymd folder to `env\Lib\site-packages\kivymd`
    - Windows: `xcopy kivymd\* env\Lib\site-packages\kivymd\ /E`
    - Linux: `cp kivymd/* env/Lib/site-packages/kivymd/`
- Make a file named `set_web_api_key.py` with the following content:
```py
import os
os.environ["WEB_API_KEY"] = "[YOUR WEB API KEY HERE]" # Find web api key in firebase project settings
```
- To sanity check if everything is working fine, run `python main.py` and see if the app runs.
- Also you can run `pip list` to see if only the packages in `requirements.txt` are installed.

## Packaging 📦
#### PyInstaller (Windows & Linux)
- Run `copy_kv_files.py` to copy kv files to `all_files` folder that will be used by PyInstaller.
    - NOTE: Do this every time you make changes to kv files.
- Make sure environment is activated if not run `env\Scripts\activate`.
- Pyinstaller command to package app:
    - Windows `pyinstaller passlock_windows.spec --noconfirm`
    - Linux `pyinstaller passlock_linux.spec --noconfirm`
- Output will be in `dist/passlock` folder.

##### Advanced Installer (Windows only MSI Build)
- Download and install <a href="https://www.advancedinstaller.com/downloads.html">Advanced Installer</a>.
- Check to see if path is correct for advanced installer in `make_msi_build.bat` file.
- Run `make_msi_build.bat` to make MSI installer.
- Output will be in `Passlock-SetupFiles` folder.
- Run `Passlock-SetupFiles\Passlock.msi` to install and run app.

##### Linux tar.gz build
- Docs coming soon... (For now you can use PyInstaller and make a tar.gz file manually)

## Screenshots 💻
<h4 align = "center"> Signup with Passlock </h4>
<p align="center">
    <img src = "./screenshots/WelcomeScreen.png" width = 400>
    <img src = "./screenshots/Manual.png" width = 400>
</p>

<h4 align = "center"> Create Strong Passwords </h4>
<p align="center">
    <img src = "./screenshots/DarkMode.png" width = 400>
    <img src = "./screenshots/FindScreen.png" width = 400>
</p>

<h4 align = "center"> Backup and Sync </h4>
<p align="center">
    <img src = "./screenshots/sync.png" width=400>
    <img src = "./screenshots/colors.png" width=400>
</p>


## Frameworks ⚙️
Made with 💖 in Python using <a href="https://github.com/kivy/kivy">Kivy</a> as framework, along with
<a href="https://github.com/kivymd/KivyMD">KivyMD</a> library.


