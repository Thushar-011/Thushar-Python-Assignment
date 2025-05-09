import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    if username in users:
        print("User already exists.")
    else:
        users[username] = hash_password(password)
        print("Created new user")

def login_user(username, password):
    if username not in users:
        print("User not found")
    elif users[username] == hash_password(password):
        print("Login Successful")
    else:
        print("Incorrect password")

while True:
    print("\nChoose an option: register / login / exit")
    option = input("Your choice: ").strip().lower()

    if option == "register":
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        register_user(uname, pwd)

    elif option == "login":
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        login_user(uname, pwd)

    elif option == "exit":
        print("Exiting program.")
        break

    else:
        print("Invalid option. Please try again.")
