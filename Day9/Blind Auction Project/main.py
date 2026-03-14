import art

print(art.logo)
# TODO-1: Ask the user for input
cont = True
bid = {}
while cont:
    name = input("Name?\n")
    price = int(input("Price?\n"))
    # TODO-2: Save data into dictionary {name: price}
    bid[name] = price
    # TODO-3: Whether if new bids need to be added
    more_bidders = input("More bidders? (y/n)\n").lower()
    if more_bidders == "n":
        cont = False
    print("\n" *100)

# TODO-4: Compare bids in dictionary
max_bid = 0
max_person = ""
for bidder in bid:
    if bid[bidder] > max_bid:
        max_bid = bid[bidder]
        max_person = bidder
print(f"Max bidder is {max_person} with ${max_bid}")
