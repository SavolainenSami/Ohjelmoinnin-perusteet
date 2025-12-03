import hashlib
import os

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    """
    Hash the password using MD5 and return the hex digest.
    """
    return hashlib.md5(password.encode()).hexdigest()


def register(PUsername: str, PPassword: str) -> None:
    """
    Register a new user by appending their credentials to the file.
    """
    # Count existing users to assign ID
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as file:
            lines = file.readlines()
            user_id = len(lines)
    else:
        user_id = 0

    hashed_password = hash_password(PPassword)

    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{user_id}{DELIMITER}{PUsername}{DELIMITER}{hashed_password}\n")


def login(PUsername: str, PPassword: str) -> bool:
    """
    Check if the username and password match an entry in the credentials file.
    """
    if not os.path.exists(CREDENTIALS_FILE):
        return False

    hashed_input = hash_password(PPassword)

    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            user_id, username, password = line.strip().split(DELIMITER)
            if username == PUsername and password == hashed_input:
                return True

    return False


def viewProfile(PUsername: str) -> list[str]:
    """
    Return the user ID and username for the given username.
    """
    if not os.path.exists(CREDENTIALS_FILE):
        return []

    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            user_id, username, password = line.strip().split(DELIMITER)
            if username == PUsername:
                return [user_id, username]

    return []


def change_password(PUsername: str, PNewPassword: str) -> None:
    """
    Change the password for the given username.
    """
    if not os.path.exists(CREDENTIALS_FILE):
        return

    new_hashed = hash_password(PNewPassword)
    updated_lines = []

    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            user_id, username, password = line.strip().split(DELIMITER)
            if username == PUsername:
                updated_lines.append(
                    f"{user_id}{DELIMITER}{username}{DELIMITER}{new_hashed}\n"
                )
            else:
                updated_lines.append(line)

    with open(CREDENTIALS_FILE, "w") as file:
        file.writelines(updated_lines)
