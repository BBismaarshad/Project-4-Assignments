import hashlib

def hash_password(password):
    """Returns the SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """Check if the password's hash matches the stored hash for the email."""
    if email in stored_logins:
        stored_hash = stored_logins[email]
        input_hash = hash_password(password_to_check)
        return stored_hash == input_hash
    return False

def main():
    # Example usage
    stored_logins = {
        "user@example.com": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
        "admin@example.com": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
    }
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.")

if __name__ == '__main__':
    main()