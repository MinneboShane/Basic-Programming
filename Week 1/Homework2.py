cost_trouser = 70.5
cost_tshirt = 20.89
cost_vest = 100.3

print("*** Welcome to the checkout system. ***")
number_trousers = int(input("How many trousers have been bought? "))
number_tshirts = int(input("How many T-shirts have been bought? "))
number_vests = int(input("How many vests have been bought? "))

total_amount = (cost_trouser * number_trousers) + (cost_tshirt * number_tshirts) + (cost_vest * number_vests)

print(f"Total amount to pay: {total_amount:.2f}")