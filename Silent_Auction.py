#!/usr/bin/python3
"""This simple code intends to automate and find the highest bidder"""
import os  # we import os and use the command cls to clear the screen after you bid to promote secrecy
print("******Welcome to the Silent Auction*****")


def find_winner(bid_details):  # we define a function to find a winner or highest bidder
    highest_bid = 0
    winner = ""
    for bidder in bid_details:  # we iterate through the bidding details to find the highest bid
        bidding_price = bid_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price  # we store the highest bid price in this variable
            winner = bidder  # we store the highest bidder in the variable winner
    print(bid_details)
    print(f"Here is the highest bidder: {winner} bid {highest_bid}")  # print the output


bidder_data = {}  # create a dictionary to hold all bidding details
more_bidders = False  # use a flag to know when to stop the program within the loop
while not more_bidders:
    name = input("What is your name?: ")  # accepting input from the users
    price = int(input("What is your bid?: "))
    bidder_data[name] = price  # storing the data in the dictionary
    new_bid = input("Are there more bidders? Type 'yes' or 'no': ").lower()  # accepting more input from the users
    if new_bid == 'no':
        more_bidders = True  # use the flag to stop the program if no
        find_winner(bidder_data)
    elif new_bid == 'yes':
        os.system('cls')  # if yes continue accepting data but with the 'cls' command it clears the screen so
    #  no one sees the screen of the previous bidders
