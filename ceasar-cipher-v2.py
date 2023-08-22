alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
 

def cipher(plain_text, shift_amount, direction_cipher):
    cipher_text = ""
    if direction_cipher == "encode":
        for letter in plain_text:
            alphabet.index(letter)
            position = alphabet.index(letter)
            new_position = (position  + shift_amount) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    elif direction_cipher == "decode":
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = abs((position - shift_amount) % 26)
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    else:
        print("Make sure you have typed the command correctly: 'encode' or 'decode'! ")
    print(f"The {direction_cipher}d text is {cipher_text}")

cipher(plain_text=text, shift_amount=shift, direction_cipher=direction)