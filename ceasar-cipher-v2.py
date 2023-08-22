logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
checker = "y"
while checker == "y":
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def cipher(plain_text, shift_amount, direction_cipher):
        cipher_text = ""
        if direction_cipher == "encode":
            for letter in plain_text:
                if letter in alphabet:
                    alphabet.index(letter)
                    position = alphabet.index(letter)
                    new_position = (position  + shift_amount) % 26
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter
                else:
                    cipher_text += letter    
        elif direction_cipher == "decode":
            for letter in plain_text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = abs((position - shift_amount) % 26)
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter
                else:
                    cipher_text += letter
        else:
            print("Make sure you have typed the command correctly: 'encode' or 'decode'! ")
        print(f"The {direction_cipher}d text is {cipher_text}")



    cipher(plain_text=text, shift_amount=shift, direction_cipher=direction)
    checker = input('Do you want to continue?\nType "y" for yes or "n" for no ')
