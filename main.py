import os
import argparse
from login import Login

parser = argparse.ArgumentParser(description="Login using username and password.")
parser.add_argument("-u", "--username", type=str, help="Username for login")
parser.add_argument("-p", "--password", type=str, help="Password for login")

args = parser.parse_args()

USERNAME = args.username or os.getenv("USERNAME")
PASSWORD = args.password or os.getenv("PASSWORD")


if not USERNAME or not PASSWORD:
    raise ValueError(
        "USERNAME and PASSWORD must be set via arguments, environment variables, or config.py"
    )

try:
    user = Login(USERNAME, PASSWORD)
    print(user.login())
except Exception as e:
    print(e)
