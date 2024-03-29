from kivy.logger import Logger
from kivy.network.urlrequest import UrlRequest

from libs.utils import *

WEB_API_KEY = os.environ["WEB_API_KEY"]
DATABASE_URL = os.environ["DATABASE_URL"]


class Firebase:
    BASE_URL = "https://www.googleapis.com/identitytoolkit/v3/relyingparty"
    SIGNUP_URL = f"{BASE_URL}/signupNewUser?key="
    LOGIN_URL = f"{BASE_URL}/verifyPassword?key="
    DELETE_URL = f"{BASE_URL}/deleteAccount?key="

    def signup_success(self, req, result):
        """
        Implement this method to handle the result of the successful signup request.
        """
        Logger.warn("Firebase: Signup success not implemented")

    def signup_failure(self, req, result):
        """
        Implement this method to handle the result of the signup failure request.
        """
        Logger.warn("Firebase: Signup failure not implemented")

    def signup(self, name, password):
        """
        Used to signup the user.
        """
        url = self.SIGNUP_URL + WEB_API_KEY
        data = json.dumps(
            {"email": name, "password": password, "returnSecureToken": True}
        )
        UrlRequest(
            url,
            req_body=data,
            on_success=self.signup_success,
            on_failure=self.signup_failure,
            timeout=15,
        )

    def login_success(self, req, result):
        """
        Implement this method to handle the result of the successful login request.
        """
        Logger.warn("Firebase: Login success not implemented")

    def login_failure(self, req, result):
        """
        Implement this method to handle the result of the login failure request.
        """
        Logger.warn("Firebase: Login failure not implemented")

    def login(self, name, password):
        """
        Used to login the user.
        """

        url = self.LOGIN_URL + WEB_API_KEY
        data = json.dumps(
            {"email": name, "password": password, "returnSecureToken": True}
        )
        UrlRequest(
            url,
            req_body=data,
            on_success=self.login_success,
            on_failure=self.login_failure,
            timeout=10,
        )

    def backup_success(self, req, result):
        """
        Override this method to handle the result of the successful backup request.
        """
        Logger.warn(f"Firebase: Backup success not implemented, {result}")

    def backup_failure(self, req, result):
        """
        Override this method to handle the result of the failure in backup request.
        """
        Logger.warn(f"Firebase: Backup failure not implemented, {result}")

    def backup(self):
        """
        Used to backup the user's passwords.
        """
        result = load_passwords()
        _json = {get_uid(): result}
        UrlRequest(
            f"{DATABASE_URL}/.json",
            req_body=json.dumps(_json),
            req_headers={"Content-type": "application/json", "Accept": "text/plain"},
            on_success=self.backup_success,
            on_failure=self.backup_failure,
            on_error=self.backup_failure,
            method="PATCH",
        )

    def restore_success(self, req, result):
        """
        Override this method to handle the result of the successful restore request.
        """
        Logger.warn(f"Firebase: Restore success not implemented, {result}")

    def restore_failure(self, req, result):
        """
        Override this method to handle the result of the failure in restore request.
        """
        Logger.warn(f"Firebase: Restore failure not implemented, {result}")

    def restore(self, user_id=None):
        """
        Used to restore the user's passwords.
        """
        if user_id is None:
            user_id = get_uid()

        UrlRequest(
            f"{DATABASE_URL}/{user_id}.json",
            on_success=self.restore_success,
            on_failure=self.restore_failure,
            on_error=self.restore_failure,
        )
