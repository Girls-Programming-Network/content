import random

# <the student's name>
print("I am a markov chain generator")
current_word = input("What word do you want to start with? ")
print(current_word, end=" ", flush = True)
cups = {"one": ["fish", "has"],
        "two": ["fish"],
        "red": ["fish"],
        "blue": ["fish"],
        "this": ["one"],
        "has": ["a"],
        "a": ["little"],
        "little": ["car"],
        "car": ["one"],
        "fish": ["two", "red", "blue", "this"]}

if current_word in cups:
  for i in range(100):
    next_word_options = cups[current_word]
    next_word = random.choice(next_word_options)
    print(next_word, end=" ", flush = True)
    current_word = next_word
# plus extension
else:
  print("\nSorry, you can't use that as a starting word.")
