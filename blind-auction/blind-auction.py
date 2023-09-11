import math
import os
def clear(): os.system('cls') 

from art import logo
print(logo)
print("Welcome to the secret auction program ")
checker = "yes"
auction_dict = {}

def auction():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction_dict[name] = bid
    

while checker == "yes":
    auction()
    checker = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    clear()

winner = max(auction_dict, key = auction_dict.get)
print(f"The winner is {winner} with a bid of ${auction_dict[winner]}")




