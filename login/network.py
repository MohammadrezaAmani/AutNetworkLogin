from requests import post


class Login:
    URL = "https://login.aut.ac.ir/login"

    def __init__(self, username: str, password: str, autologin: bool = True) -> None:
        self.username = username
        self.password = password
        self.autologin = autologin

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username_value):
        if not isinstance(username_value, (str, int)):
            raise BaseException(
                "username must be str or int not,", type(username_value)
            )
        self._username = username_value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password_value):
        if not isinstance(password_value, (str, int)):
            raise BaseException("password must be str or int,", type(password_value))
        self._password = password_value

    def login(self):
        data = {
            "username": self.username,
            "password": str(self.password),
            "dst": "",
            "popup": False,
            "erase-cookie": False,
        }
        return post(url=self.URL, data=data).status_code
