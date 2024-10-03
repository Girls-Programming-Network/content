#Password cracker workbook P solution

### Creating a rainbow table,
### i.e. a database of common passwords and their hash values
### this hashes the common passwords, and compares it to the hashed values attached to account names
### it then returns any matches 

import hashlib

rainbow = {}

#Note: You may have to adjust filepath
for line in open("Password_Cracker/CodeSolutions/rainbow_tables/common-passwords.txt"):
    password = line.strip()

    password_encoded = password.encode()
    password_hashed = hashlib.md5(password_encoded).digest()
    password_hashed_string = str(password_hashed)

    rainbow[password_hashed_string] = password

#print(rainbow)

#Note: You may have to adjust filepath
for line in open("Password_Cracker/CodeSolutions/rainbow_tables/accounts.txt"):
    line = line.strip()
    account = line.split(",")
    name = account[0]
    password_hash = account[1]

    if password_hash in rainbow:
        print("Name:",name)
        print("Password:",rainbow[password_hash] +"\n")