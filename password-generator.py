special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', ',', '.', ';', ':', '?', '<', '>', '/', '\\', '|', '_', '+', '=', '-', '`', '~']

char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

import random

nr_special = int(input("How many symbols would you like?\n"))
nr_char = int(input("How many letters would you like?\n"))
nr_dig = int(input("How many numbers would you like?\n"))
pass_special=""
pass_char=""
pass_dig=""
for special_characters in range(1, nr_special+1):  
    pass_special += random.choice(special)

for characters in range(1, nr_char+1):  
    pass_char += random.choice(char)

for digits in range(1, nr_dig+1):
    pass_dig += random.choice(dig)

password = pass_special + pass_char + pass_dig
npassword = "".join(random.sample(password, len(password)))
print(npassword)