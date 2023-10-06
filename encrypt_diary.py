import os
from datetime import date
from cryptography.fernet import Fernet


# creating a python program that creates a diary entry and then encrypt or decrypt the entry
# create the folder on my desktop
def create_diary():
    path = "C://Path//You//Want//Diary"
    try:
        directory_name = "Diary"
        path = os.path.join(path, directory_name)
        os.mkdir(path)
        print(f"Directory {directory_name} made")
    except FileExistsError:
        return path
    return path


# create and write the file
def create_entry():
    today = date.today()
    entry = str(today) + ".txt"
    return entry


def write_entry():
    content = input("What do you want to write about?\n")
    return content


# encrypting the file with symmetric encryption

# create the key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as filekey:
        filekey.write(key)


def load_key():
    return open("key.key", "rb").read()


def encryption(file, key):

    f = Fernet(key)
    with open(file, "rb") as file:
        file_read = file.read()
        encrypted = f.encrypt(file_read)
        return encrypted


# create the function that can decrypt the file if needed


def decryption(file, key):

    f = Fernet(key)
    with open(file, 'rb') as file:
        encrypted_file = file.read()
        decrypted_data = f.decrypt(encrypted_file)
        print(decrypted_data)


def main():
    os.chdir(create_diary())
    file = create_entry()
    with open(file, 'a') as f:
        f.write(write_entry())
    # The write key function should be commented out if this program was run more than once
    write_key()
    key = load_key()
    encrypted_entry = encryption(file, key)

    with open(file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_entry)

    decryption(file, key)


if __name__ == "__main__":
    main()
