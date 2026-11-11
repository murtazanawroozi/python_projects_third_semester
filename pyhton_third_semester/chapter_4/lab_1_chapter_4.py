class InvalidUsernameError(Exception):
    pass

while True:
    try:
        username = input("Enter username: ")
        if len(username) < 3:
            raise InvalidUsernameError("Username must be at least 3 characters.")
        
        age = int(input("Enter age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
            
    except (InvalidUsernameError, ValueError) as error:
        print("Registration failed:", error)
        
    else:
        print("Registration successful for:", username)
        break
        
    finally:
        print("Completed status check.")