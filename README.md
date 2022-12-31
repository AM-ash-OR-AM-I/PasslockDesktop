<p align = "center">
    <img src = "icons/pass.png" height = 150>
</p>

Passlock for PC - A powerful cross-platform password manager.
<h4>
    <a href="https://github.com/AM-ash-OR-AM-I/Passlock">
        Check out Passlock for Android
    </a>
</h4>

# Features 🌟
* Backup and sync passwords across devices 💻📱.
* Encrypted passwords using AES 128bit for maximum security.
* Mimics Material v3 Monet engine with 🌙 Dark Mode, to use different 🎨 color themes. (Self-made)
* Make strong passwords 🔑 through built in password generator.
* Advanced 🔍 finding algorithm to search for passwords easily.

# Installation/Releases 🚀
<h4>
    <a href="https://github.com/AM-ash-OR-AM-I/PasslockDesktop/releases">
        Check out Releases and Download for linux/windows 🧑🏻‍💻
    </a>
</h4>

## Additional (optional) steps for linux 
After installing and extracting .tar.gz file in linux to run app anywhere in terminal we can create a softlink like this:

### Run anywhere
```$ ln -s /path/to/passlock/Passlock /usr/local/bin/passlock```

After this we can run passlock by typing `$ passlock`

### Add menu icon

```
$ cd ~/.local/share/applications
$ nano passlock.desktop
```
Paste the following lines by specifying the `/path/to/passlock`
```
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

# Screenshots 💻
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


# Frameworks ⚙️
Made with 💖 using Python using <a href="https://github.com/kivy/kivy">Kivy</a> as framework, along with
<a href="https://github.com/kivymd/KivyMD">KivyMD</a> library.
