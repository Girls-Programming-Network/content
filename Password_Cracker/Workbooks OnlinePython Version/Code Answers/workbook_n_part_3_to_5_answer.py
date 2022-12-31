import hashlib

salted_passwords = []

for line in open("salty-accounts.txt"):
    line = line.strip()
    account = line.split(",")
    password_hash = account[1]
    salted_passwords.append(password_hash)

for salt in range(1000, 10000):
    possible_salted = "password" + str(salt)
    possible_encoded = possible_salted.encode()
    possible_hashed = hashlib.md5(possible_encoded).digest()
    possible_hashed = str(possible_hashed)

    if possible_hashed in salted_passwords:
        print(salt)
        break
