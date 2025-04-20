user_db = {
    "sahil": "sahil@1234",
    "aditya": 'aditya@256',
    "rushi": "rushi@1234"
}

MAX_ATTEMPTS = 3

def login():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        try:
            username = input("Enter your username: ")
            if not username.isalnum():
                raise ValueError("Username should be alphanumeric.")
            
            if username not in user_db:
                raise KeyError("User does not exist.")
            
            password = input("Enter your password: ")
            if user_db[username] != password:
                raise PermissionError("Incorrect password")
            
            print("Login Successful. Welcome,", username + '!')
            return
        
        except ValueError as ve:
            print("ValueError: ", ve)

        except KeyError as ke:
            print("KeyError:", ke)

        except PermissionError as pe:
            print("PermissionError:", pe)

        except Exception as e:
            print("An unexpected error occurred:", e)

        attempts += 1
        print(f"Attempts left: {MAX_ATTEMPTS - attempts}\n")

    print("Too many failed attempts. Please try again later.")


login()

        
            
        