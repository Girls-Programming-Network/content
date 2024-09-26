#Password cracker workbook 3 part 3-5 solution 

#Finding which salt was used to hash the salted passwords
import hashlib

salted_passwords = []

#Note: You may have to adjust filepath
for line in open("Password_Cracker/CodeSolutions/rainbow_tables/salty-accounts.txt"):
    #Take all the hashed values from file and store in list
    line = line.strip()
    account = line.split(",")
    password_hash = account[1]
    salted_passwords.append(password_hash)

# generate salt value (number 1000-10000)
# adds salt + password then hashes it. 
# returns if this matches the hashed value in salty-accounts 
for salt in range(1000, 10000):
    possible_salted = "password" + str(salt)
    possible_encoded = possible_salted.encode()
    possible_hashed = hashlib.md5(possible_encoded).digest()
    possible_hashed = str(possible_hashed)

    if possible_hashed in salted_passwords:
        print(salt)
        break
