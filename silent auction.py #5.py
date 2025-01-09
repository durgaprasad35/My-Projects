import os
def function(bidder_details):
 
 winner = ""
 highest_bid = 0
      
 for bidder in bidder_details:
        
        bidder_price = bidder_details[bidder]

        if bidder_price > highest_bid:
            bidder_price = highest_bid
            winner = bidder
        print(f"The winner is {winner} with bid price {highest_bid} ")

bidder_data = {}
end_of_bid = False

while not end_of_bid:
    name= input("Enter bidder name : ")

    price = int(input("Enter your bid price: "))

    bidder_data[name] = price

    more_bidders = input("Is there any bitters type yes otherwise no : ")

    if more_bidders == "no":
        end_of_bid = True
        function(bidder_data)
    elif more_bidders == "yes":
        os.system('cls')
    