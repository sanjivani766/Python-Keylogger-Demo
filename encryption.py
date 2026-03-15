from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_log():

    key = load_key()
    fernet = Fernet(key)

    with open("logs/activity_log.txt", "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open("logs/activity_log.txt", "wb") as f:
        f.write(encrypted)