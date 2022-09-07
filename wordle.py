import os
import requests
import random
import re

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
words = response.text.split("\n")
word = str(words[random.randint(0, 10000)])
word_length = len(word)
print('[ debug ] the word is ' + word)

new_word = ''
tries = 0
max_tries = 10 # Word length + max tries

for i in word:
    new_word += '_'

print(new_word)
while new_word not in word:
    chosen = input('Letter: ')

    if len(chosen) != 1:
        continue

    if tries == word_length + max_tries:
        break
    tries += 1

    if chosen in word:
        new_word = new_word[0:word.index(chosen)] + chosen + new_word[word.index(chosen)+1: ]
    
    print(new_word)


if tries != word_length + max_tries:
    print('You found the word, it was: ' + word)

print('You lost! The word was ' + word)