from auction_art import logo

print(logo)
auctioners = []
another_bidder = True
bigBid = 0.0

while another_bidder:
    new_auctioner = {}
    new_auctioner["name"] = input("What's your name? ")
    new_auctioner["bid"] = float(input("What's your bid? "))
    auctioners.append(new_auctioner)
    another_bidder = input("Is there another_bidder?\n")

    if another_bidder.lower() == 'no':
        another_bidder = False

for i in range(0, len(auctioners)):
    if auctioners[i]["bid"] > bigBid:
        bigBid = auctioners[i]["bid"]
        bigBidder = auctioners[i]["name"]

print(f"winner is {bigBidder}, with {bigBid}")
