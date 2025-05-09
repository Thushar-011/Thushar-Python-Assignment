users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

def add_user():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    email = input("Enter Email: ")

    for user in users:
        if user['id'] == id:
            print(" User ID already exists.")
            return
    users.append({"id": id, "name": name, "email": email})
    print(" User added.")

def get_user():
    id = int(input("Enter ID to retrieve: "))
    for user in users:
        if user['id'] == id:
            print(" User found:", user)
            return
    print(" User not found.")

def update_user():
    id = int(input("Enter ID to update: "))
    for user in users:
        if user['id'] == id:
            name = input("Enter new name (press Enter to skip): ")
            email = input("Enter new email (press Enter to skip): ")
            if name:
                user['name'] = name
            if email:
                user['email'] = email
            print(" User updated.")
            return
    print(" User not found.")

def delete_user():
    id = int(input("Enter ID to delete: "))
    for user in users:
        if user['id'] == id:
            users.remove(user)
            print(" User deleted.")
            return
    print(" User not found.")

def menu():
    while True:
        print("\n--- User CRUD Menu ---")
        print("1. Add User")
        print("2. Get User by ID")
        print("3. Update User")
        print("4. Delete User")
        print("5. Show All Users")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            get_user()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print(" All Users:", users)
        elif choice == "6":
            print(" Exiting program.")
            break
        else:
            print(" Invalid choice. Try again.")


menu()
