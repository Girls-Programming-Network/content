#Password cracker workbook 3 part 6 solution

# Finding our salted password with our rainbow table
# this hashes the common passwords, and compares it to the salted-hashed values attached to account names
# it then returns any matches 
import hashlib

salt = "7549" #this is the salt found from workbook 3 part 3-5

rainbow = {}
#Note: You may have to adjust filepath 
for line in open("Password_Cracker/CodeSolutions/rainbow_tables/common-passwords.txt"):
    #salt and then hash the common passwords
    password = line.strip() + salt

    password_encoded = password.encode()
    password_hashed = hashlib.md5(password_encoded).digest()
    password_hashed_string = str(password_hashed)

    rainbow[password_hashed_string] = password

#print(rainbow)

#Note: You may have to adjust filepath
for line in open("Password_Cracker/CodeSolutions/rainbow_tables/salty-accounts.txt"):
    line = line.strip()
    account = line.split(",")
    name = account[0]
    password_hash = account[1]

    if password_hash in rainbow:
        #Note: this prints the password with the salt still appended
        print("Name:",name)
        print("Password:",rainbow[password_hash] +"\n")
