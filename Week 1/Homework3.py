cost_trouser = 70.5
cost_tshirt = 20.89
cost_vest = 100.3

print("*** Welcome to the checkout system. ***")
number_trousers = int(input("How pairs of trousers have been bought? "))
number_tshirts = int(input("How many T-shirts have been bought? "))
number_vests = int(input("How many vests have been bought? "))

print(f"You have bought:\n\t Trousers: {number_trousers} pair(s)\n\t T-shirts: {number_tshirts} piece(s)\n\t Vests: {number_vests} piece(s)")


total_amount = (cost_trouser * number_trousers) + (cost_tshirt * number_tshirts) + (cost_vest * number_vests)

print(f"Total: {total_amount:.2f}")