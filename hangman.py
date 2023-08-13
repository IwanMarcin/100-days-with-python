import random
word_list = ["apple", "banana", "carrot", "dog", "elephant", "fish", "grape", "hamburger", "house", "jacket", "kite", "lemon", "moon", "notebook", "orange", "pencil", "queen", "rainbow", "sun", "tree"]
word = random.choice(word_list) 
visible = []
n = 0
while n < len(word):
    visible.append("_")
    n += 1

letters_in_word = list(word)
life = 7
print("Welcome to The Hangman Game!\n")
print(f"Your word is {n} letters long and you have {life} lives left!")

used = ""

while  life >= 0:
    print(" ".join(visible))
    if "".join(visible) == word:
        print("Congratulations, you won!")
        break
    elif life == 0:
        print(f"Unfortunately, you lost this time! That word was: {word_list}")
        break
    else:
        letter = input("Please type any letter from a to z \n").lower()
        if letter in used:
            print("You've already used this letter, try typing any other!\n")   
        elif len(letter) != 1:
            print("You have to type exactly one letter!")
        elif letter not in word:
            life = life - 1
            used += letter
            print(f"Your letter is not in the word, you lose one life. You have {life} life/lives left")
        else:
            used += letter
            n = 0
            while n < len(letters_in_word):
                if letter == letters_in_word[n]:
                    visible[n] = letter
                    n += 1
                else:
                    n += 1
            


                        
