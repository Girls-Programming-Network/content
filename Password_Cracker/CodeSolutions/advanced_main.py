#Password cracker workbook 3 part 1-2

#Salting our own password
import hashlib

salt = "salty"

##Salt and then hash the passphrase to get updated hash value

# correct = "The ship sails at midnight" + salt
# correct_encoded = correct.encode()
# correct_salted_hash = hashlib.md5(correct_encoded).digest()
# print(correct_salted_hash)


#new salted hash value of our passhphrase
correct_hashed = b"\xae\xbc\xe9f\xd1%Q\x8a\xf2\xfd\xba\xb2\x922`\xa5"

guess = input("What is the passphrase? ") + salt
guess_encoded = guess.encode()
guess_hashed = hashlib.md5(guess_encoded).digest()

if correct_hashed == guess_hashed:
    print("Welcome to the club!")
else:
    print("Go away!")
