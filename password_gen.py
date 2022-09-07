import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

length = int(input('Password length: '))

random.shuffle(characters)
password = []

for character in range(length):
    password += (random.choice(characters))

random.shuffle(password)

print("".join(password))