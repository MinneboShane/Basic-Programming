land_price = float(input("Price of the land? "))
building_price = float(input("Price of the building? "))

total_cost = building_price + land_price
total_cost += total_cost * 0.21

print(f"The total cost of this project is {total_cost:.2f}")
