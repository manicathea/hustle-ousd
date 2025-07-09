#Debugging Activity - Manica Thea

#Code snippet 1 
#ZeroDivisionError - Fixed by changing the zero because you can't divide by zero
x = 10
y = 2 
result = x / y 
print("Result:", result)


#Code snippet 2 
#IndexError - Fixed by taking out the +1
numbers = [1, 2, 3, 4 ,5]
for i in range(len(numbers)):
    print(numbers[i])


#Code snippet 3 
#SyntaxError - Fixed by adding a colon 
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
radius = 5
print(calculate_area(radius))


#Code snippet 4
#SyntaxError - Fixed by adding a colon
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))


#Code snippet 5
#SyntaxError - Fixed by adding a colon
for i in range(5):
   print(i)


#Code snippet 6
#SyntaxError - Fixed by adding + name
def greet(name):
   return "Hello, " + name
name = "manica"
print(greet(name))


#Code snippet 7 
#IndentationError - Fixed by adding an indentation 
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
   sum += number
print("Sum of numbers:", sum)


#Code snippet 8
#RecursionError - Fixed by subtracting 1 instead of adding
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
print(factorial(5))


#Code snippet 9
#LogicalError - Fixed by adding name == to bob
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print("Hello, " + name)
else:
   print("Hello, stranger!")


#Code snippet 10
#ZeroDivisionError - Fixed by changing num2 because you can't divde by zero
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 5
print(divide_numbers(num1, num2))

