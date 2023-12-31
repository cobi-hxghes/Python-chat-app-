import csv
import hashlib
import secrets


def hash_password(password, salt):
    salted_password = (password + salt).encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password


def generate_salt():
    return secrets.token_hex(16)


def check_user_credentials(username, password):
    with open('user_credentials.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Username'] == username:
                stored_password = row['HashedPassword']
                salt = row['Salt']
                hashed_password = hash_password(password, salt)
                return hashed_password == stored_password
    return False


def hash_and_salt(password):
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    return hashed_password, salt