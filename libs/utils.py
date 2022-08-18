import os.path, pickle, json
import string
import random

if not os.path.exists("data"):
    os.mkdir("data")


# Doesn't always generate alphanumeric password
def auto_password(len: int, ascii=True, digits=True, special_chars=True) -> str:
    sample =random.sample(
        string.ascii_letters * ascii, 20*ascii
            ) + random.sample(
                string.digits * digits, 10*digits
            )+ random.sample(
                string.punctuation * special_chars, 10*special_chars
            )
    if sample:
        random_pass = "".join(random.sample(sample, len))
    else:
        random_pass = ""
    return random_pass


def load_passwords() -> dict:
    if os.path.exists("data/passwords"):
        with open("data/passwords", "rb") as f:
            encrypted_pass = pickle.load(f)
        return encrypted_pass
    else:
        return {}


def get_uid() -> str:
    with open("data/user_id.txt", "r") as f:
        uid = f.read()
    return uid


def write_passwords(dictionary: dict) -> None:
    with open("data/passwords", "wb") as f:
        pickle.dump(dictionary, f)


def remove_user_data() -> None:
    if os.path.exists("data/user_id.txt"):
        os.remove("data/user_id.txt")
    if os.path.exists("data/passwords"):
        os.remove("data/passwords")
    if os.path.exists("data/encrypted_file.txt"):
        os.remove("data/encrypted_file.txt")


def __get_config() -> dict:
    if os.path.exists("data/config.json"):
        with open("data/config.json", "r") as f:
            config = json.load(f)
        return config
    else:
        return {}


def get_email() -> str:
    if os.path.exists("data/email.txt"):
        with open("data/email.txt", "r") as f:
            email = f.read()
        return email
    else:
        return "DemoMail"


def get_primary_palette() -> str:
    if os.path.exists("data/config.json"):
        with open("data/config.json", "r") as f:
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
    return json_data.get("auto_sync", False)

def get_scaling() -> str:
    json_data = __get_config()
    return str(json_data.get("ui_scaling", 1.5))
    
