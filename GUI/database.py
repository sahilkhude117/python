import sqlite3

conn = sqlite3.connect('users_management.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')
conn.commit()

def add_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))

    try:
        cursor.execute("INSERT INTO users (username, email, age) VALUES (?,?,?)", (username, email, age))
        conn.commit()
        print("user added successfully")
    except sqlite3.IntegrityError:
        print("Error: Username already exists!")

def show_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    if users:
        print("\n User List: ")
        for user in users:
            print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Age: {user[3]}")
    else:
        print("No users found!")

def delete_user():
    username = input("Enter username to delete: ")
    cursor.execute("DELETE FROM users WHERE username = ? ", (username,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"User '{username}' deleted successfully!")
    else:
        print("User not found!")

def update_user():
    username = input("Enter username to update: ")
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        print(f'Current details: Username: {user[1]}, Email: {user[2]}, Age: {user[3]}')
        email = input("Enter new Email: ")
        age = int(input("Enter new age: "))
        cursor.execute("UPDATE users SET email = ?, age = ? WHERE username = ?", (email, age, username))
        conn.commit()
        print("User details updated successfully!")
    else:
        print("User not found!")

def search_user():
    username = input("Enter username to search: ")
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        print(f'User found: ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Age: {user[3]}')
    else:
        print("User not found!")

def menu():
    while True:
        print("\nUser Management System")
        print("1. Add User")
        print("2. Show All Users")
        print("3. Delete User")
        print("4. Update User")
        print("5. Search User")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            show_users()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            update_user()
        elif choice == "5":
            search_user()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


menu()

conn.close()
