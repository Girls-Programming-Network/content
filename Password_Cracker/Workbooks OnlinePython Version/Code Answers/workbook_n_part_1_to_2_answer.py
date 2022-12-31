import hashlib

salt = "salty"

correct_hashed = b"\xae\xbc\xe9f\xd1%Q\x8a\xf2\xfd\xba\xb2\x922`\xa5"

guess = input("What is the passphrase? ") + salt
guess_encoded = guess.encode()
guess_hashed = hashlib.md5(guess_encoded).digest()

if correct_hashed == guess_hashed:
    print("Welcome to the club!")
else:
    print("Go away!")
