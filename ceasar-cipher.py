alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    index_list = []
    for i in range (0, len(text)):
        if text[i] in alphabet:
            index_list.append(alphabet.index(text[i]))

    for i in range (0, len(index_list)):
        index_list[i]+= shift
        
    for i in range (0, len(index_list)):
        while index_list[i] > 25:
            index_list[i]-= 26
        
    encrypt_letters = []
    for i in range (0, len(index_list)):
        encrypt_letters.append(alphabet[index_list[i]])

    encrypt_letters = "".join(encrypt_letters)
    print(f"The encoded text is {encrypt_letters}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    print("Sorry, this feature has not been written yet 😔")
else:
    print("Make sure you have typed the command correctly: 'encode' or 'decode'! ")