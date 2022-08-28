auction_list=[]

def auction_function(person_name,amount_of_auction):
    auction_dict={}
    auction_dict[person_name]=amount_of_auction
    auction_list.append(auction_dict)
#     print(auction_dict)

auction_continue="yes"

while auction_continue=="yes":
    auction_continue=input("if auction has to be continued then press 'yes' for closing press 'no'")
    if auction_continue=="yes":
        name=input("enter the name")
        amount=int(input("enter the amount"))
        auction_function(person_name=name,amount_of_auction=amount)
#         print(auction_list)

    else:
        all_amounts=[]
        for x in auction_list:
            all_amounts+=x.values()
            top=max(all_amounts)
            y=all_amounts.index(top)
            if top in x.values():
                top_bidder=auction_list[y]
              
        print(all_amounts)
        print(top)
        print(f"top bidder of the auction is {top_bidder.keys()} and amount is {top_bidder.values()}")
            