import hashlib

salt = "7549"

rainbow = {}
for line in open("common-passwords.txt"):
    password = line.strip() + salt

    password_encoded = password.encode()
    password_hashed = hashlib.md5(password_encoded).digest()
    password_hashed_string = str(password_hashed)

    rainbow[password_hashed_string] = password

print(rainbow)

for line in open("salty-accounts.txt"):
    line = line.strip()
    account = line.split(",")
    name = account[0]
    password_hash = account[1]

    if password_hash in rainbow:
        print(name)
        print(rainbow[password_hash])
