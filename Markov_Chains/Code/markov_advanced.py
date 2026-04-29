import random

# Reading a file: (or more files if previous part is done)
with open("intermediate_winnie_the_pooh.txt", "r") as input_file:
	source_text = input_file.read()


# Training:
cups = {}
split_text = source_text.split()
num_words = len(split_text)

for num in range(num_words-2):
    current_pair =  split_text[num] + " " + split_text[num+1]
    current_word = split_text[num+1]
    next_word = split_text[num + 2]
        
    if current_pair not in cups:
        cups[current_pair] = [next_word]
    else:
        cups[current_pair].append(next_word)

    if current_word not in cups:
        cups[current_word] = [next_word]
    else:
        cups[current_word].append(next_word)


# Start the program
print("I am a markov chain generator.")
current_word = input("What word do you want to start with? ")

# Generating:
print(current_word, end=" ")
current_pair = current_word
for i in range(100):
    next_word_options = None
    if current_pair in cups:
            next_word_options = cups[current_pair]
    elif current_word in cups:
            next_word_options = cups[current_word]
    if next_word_options:  #students can also check for empty
        next_word = random.choice(next_word_options)
        print(next_word, end=" ")           	 
        current_pair = current_word + " " + next_word
        current_word = next_word