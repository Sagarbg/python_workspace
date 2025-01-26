import auction_art
bidder = True

name = ""
bid_amt = ""

bidders = {}

print(auction_art.logo)

def find_highest_bidder (bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print("The winner is ", winner, "with a bid of Rs.", highest_bid)

while bidder:

    for i in range(bidder):
        name = input("What is your name? :")
        bid_amt = int(input("What is your bid? Rs.:"))
        bidders[name] = bid_amt

    print("Dictionary after adding user input:", bidders)

    yes_or_no = input("Are any other bidders? Type 'Yes' or 'No'. \n ").lower()

    if yes_or_no == "no":
        bidder = False
        find_highest_bidder(bidders)
        # print(bidders)
        print("Thank you..")
    elif yes_or_no == "yes":
        print("\n" * 20)


        # winner = max(zip(bidders.values(), bidders.keys()))[1]
        
        # print("The winner is ", winner, "with a bid of Rs.", bidders[winner])