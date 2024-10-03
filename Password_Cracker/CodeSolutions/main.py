#Password cracker workbook G solution 

#Hashing a password and comparing it to the input
import hashlib

#The following section gets deleted by the students - it finds the hashed version of the passphrase

##correct = "The ship sails at midnight"
##correct_encoded = correct.encode()
##print(type(correct_encoded))
##correct_hashed = hashlib.md5(correct_encoded).digest()
##print(correct_hashed)

#Note: The correct passphrase is "The ship sails at midnight"
correct_hashed = b"\xcc\xd6R\x16\xb9\x1bP~lK\x01\x0e\x063\x10\xec"

guess = input("What is the passphrase? ")
guess_encoded = guess.encode()
guess_hashed = hashlib.md5(guess_encoded).digest()

#if the hashed versions are the same, then the passphrases must have been the same
if guess_hashed == correct_hashed:
    print("Welcome to the club!")
else:
    print("Go away!")
