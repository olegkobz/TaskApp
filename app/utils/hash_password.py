import bcrypt
def hashing_password(password):
    pass_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    pass_hash = bcrypt.hashpw(pass_bytes, salt)
    return pass_hash.decode("utf-8")