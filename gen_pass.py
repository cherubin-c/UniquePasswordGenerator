import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    
    # Create a pool of characters based on user preferences
    character_pool = ""
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # User input for password configuration
    length = int(input("Enter password length (default 12): ") or 12)
    use_uppercase = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
    use_lowercase = input("Include lowercase letters? (y/n, default y): ").lower() != 'n'
    use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
    use_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'

    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
