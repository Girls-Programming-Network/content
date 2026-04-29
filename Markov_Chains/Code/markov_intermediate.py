import random
cups = {}
source_text = """
<a bunch of text here>
"""
split_text = source_text.split()
num_words = len(split_text)
for i in range(num_words - 1):
    current_word = split_text[i]
    next_word = split_text[i+1]

    if current_word not in cups:
        cups[current_word] = [next_word]
    else:
        cups[current_word].append(next_word)

print("I am a markov chain generator")
current_word = input("What word do you want to start with? ")
print(current_word)

if current_word  in cups:
    for i in range(100):
        if current_word in cups:
            next_word_options = cups[current_word]
            next_word = random.choice(next_word_options)
            print(next_word, end=" ")
            current_word = next_word
else:
    print("\nSorry, you can't use that as a starting word!")