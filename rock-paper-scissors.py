import random
print("Let's play rock, paper, scissors!\n")
human = input("Choose what you want to show by entering one of three options: stone, paper, scissors\n").lower()

comp_ans = random.randint(1, 3)

if comp_ans == 1:
    result = "paper"
elif comp_ans == 2:
    result = "scissors"
else:
    result = "rock"

if result == "paper" and human == "paper":
    print("DRAW")
elif result == "paper" and human == "rock":
    print("COMPUTER WIN")
elif result == "paper" and human == "scissors":
    print("YOU WIN")
elif result == "scissors" and human == "scissors":
    print("DRAW")
elif result == "scissors" and human == "rock":
    print("YOU WIN")
elif result == "scissors" and human == "paper":
    print("COMPUTER WIN")
elif result == "rock" and human == "rock":
    print("DRAW")
elif result == "rock" and human == "paper":
    print("YOU WIN")
elif result == "rock" and human == "scissors":
    print("COMPUTER WIN")

