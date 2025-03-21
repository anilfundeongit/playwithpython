
bid_data = {}
keep_running = True
while(keep_running):
    name = input("What is your name?\n").lower()
    bid_amount = input("What is your bid amount RS:\n")
    bid_data[name] = bid_amount
    response = input("Do you want to put another bid? 'yes' or 'no'\n ").lower()
    if response == 'yes':
        print("\n" * 30)
        keep_running = True
    else:
        keep_running = False

highest_bid = 0
highest_bidder = ''
for name in bid_data:
    if int(bid_data[name]) > int(highest_bid):
        highest_bid = bid_data[name]
        highest_bidder = name


print(f"Highest bidder is {highest_bidder} with bid amount {highest_bid}")