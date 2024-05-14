from cryptography.fernet import Fernet

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Generate a key




# Encrypt the message
def criptare_parola(password , key):
    encrypted_password = encrypt_message(password, key)
    return encrypted_password

# Decrypt the message
def decriptare_parola(encrypted_password , key):
    decrypted_password = decrypt_message(encrypted_password, key)
    return decrypted_password
