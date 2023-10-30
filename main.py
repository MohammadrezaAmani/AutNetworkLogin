from login import Login

try:
    from config import PASSWORD, USERNAME
except:
    raise BaseException("set your `USERNAME` and `PASSWORD` at `config.py` file.")

try:
    user = Login(USERNAME, PASSWORD)
    print(user.login())
except Exception as e:
    print(e)
