import hashlib

correct_hashed = b"\xcc\xd6R\x16\xb9\x1bP~lK\x01\x0e\x063\x10\xec"

guess = input("What is the passphrase? ")
guess_encoded = guess.encode()
guess_hashed = hashlib.md5(guess_encoded).digest()

if correct_hashed == guess_hashed:
    print("Welcome to the club!")
else:
    print("Go away!")
