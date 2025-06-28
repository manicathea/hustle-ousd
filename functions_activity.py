#Functions Activity - Manica Thea

menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

#Calculating Total price 
def total_price(food1, food2):
    price1 = menu [food1]
    price2 = menu [food2]
    total = price1 + price2
    return total
print(total_price('Hot dog','Soda'))

#Calculating the difference 
def price_difference(food1, food2):
    price1 = menu[food1]
    price2 = menu [food2]
    difference = abs (price1 - price2)
    return difference
print(price_difference('Hot dog','Soda'))

#Inflation of a Hot dog 
def inflation(food, multiplier):
    menu[food] = menu [food] * multiplier
    return menu
print(inflation('Hot dog', 1.10))

#Deflation of a Hot dog
def deflation(item, divide):
    menu[item] = menu[item] / divide
    return menu
print(deflation('Hot dog', 1.20))

#Finding the cheapest item
def find_cheapest_item():
    cheapest_item = min(menu, key=menu.get)
    return cheapest_item
cheapest_item = find_cheapest_item()
print(cheapest_item)


