import json
import os.path
import pickle
import random
import string

if not os.path.exists(f"./data"):
    os.mkdir(f"./data")


def auto_password(length: int, letters: bool = True, digits: bool = True, special_chars: bool = True) -> str:
    universe = ""
    password = ""
    if letters:
        universe += string.ascii_letters
        password += random.choice(string.ascii_letters)
    if digits:
        universe += string.digits
        password += random.choice(string.digits)
    if special_chars:
        universe += string.punctuation
        password += random.choice(string.punctuation)

    rest = length - len(password)
    if universe == "":  # if all options are false
        return "Error: No options selected"
    for _ in range(rest):
        password += random.choice(universe)

    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    return password


def load_passwords() -> dict:
    if os.path.exists("./data/passwords"):
        with open("./data/passwords", "rb") as f:
            encrypted_pass = pickle.load(f)
        return encrypted_pass
    else:
        return {}


def get_uid() -> str:
    with open("./data/user_id.txt", "r") as f:
        uid = f.read()
    return uid


def write_passwords(dictionary: dict) -> None:
    with open("./data/passwords", "wb") as f:
        pickle.dump(dictionary, f)


def remove_user_data() -> None:
    if os.path.exists("./data/user_id.txt"):
        os.remove("./data/user_id.txt")
    if os.path.exists("./data/passwords"):
        os.remove("./data/passwords")
    if os.path.exists("./data/encrypted_file.txt"):
        os.remove("./data/encrypted_file.txt")


def __get_config() -> dict:
    if os.path.exists("./data/config.json"):
        with open("./data/config.json", "r") as f:
            config = json.load(f)
        return config
    else:
        return {}


def get_email() -> str:
    if os.path.exists("./data/email.txt"):
        with open("./data/email.txt", "r") as f:
            email = f.read()
        return email
    else:
        return "DemoMail"


def get_primary_palette() -> str:
    if os.path.exists("./data/config.json"):
        with open("./data/config.json", "r") as f:
            config = json.load(f)
        return config.get("primary_palette", "DeepOrange")
    else:
        return "DeepOrange"


def is_dark_mode(system=False) -> bool:
    json_data = __get_config()
    return json_data.get("system_dark_mode" if system else "dark_mode", False)


def is_backup_failure() -> bool:
    json_data = __get_config()
    return json_data.get("backup_failure", False)


def is_extra_security() -> bool:
    json_data = __get_config()
    return json_data.get("extra_security", False)


def check_auto_sync() -> bool:
    json_data = __get_config()
    return json_data.get("auto_sync", True)


def get_scaling() -> str:
    json_data = __get_config()
    return str(json_data.get("ui_scaling", 1.5))
