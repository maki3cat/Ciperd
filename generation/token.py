import os


def get_access_token():
    if os.path.exists("access_token.txt"):
        with open("access_token.txt", "r") as f:
            access_token = f.read().strip()
    else:
        access_token = ""
    return access_token
