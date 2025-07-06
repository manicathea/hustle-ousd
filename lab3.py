# Lab 3 Manica Thea

#Task 1
food = "spring rolls"
print(food[:3])
print(food[-3:])
first_last = food[0] + food[-1]
print (first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

#Task 2 
number_list = [12, 10, 9, 0 , 100, -1]
number_list.append(-10)
print(number_list)
number_list.insert(3, 45)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1])
print(number_list)

#Task 3 
books = {"Sisters" : "Raina Telgemeier", "The Rainbow Fish" : "Marcus Pfister", "Born a Crime" : "Trevor Noah", "The 48 Laws of Power" : "Robert Greene"} 
print (books.keys)
print(books.values())
print(books.get("Raina Telgemeier"))
books.pop('Born a Crime')
print(books)
del books[list(books.keys())[0]]
print(books)

