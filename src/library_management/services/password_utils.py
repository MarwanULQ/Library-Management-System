import bcrypt


def hash_password(password: str) -> str:
    b_password=password.encode()
    return bcrypt.hashpw(b_password, bcrypt.gensalt())

def verify_password(password: str, hashed: str) -> bool:
    b_password=password.encode()
    return bcrypt.checkpw(b_password, hashed)
