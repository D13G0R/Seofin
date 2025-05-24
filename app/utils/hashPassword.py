from argon2 import PasswordHasher

ph = PasswordHasher()

def hashing_password(password : str):
    passwordHash = ph.hash(password)
    print (f"Contraseña normal: {password},\n Contraseña hasheada{passwordHash}")
    return passwordHash