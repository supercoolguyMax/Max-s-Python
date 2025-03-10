
#ask the user for their name and favorite number 
name = input("what is your name? ")
number1 = int(input("What is your favourite number? "))
number2 = int(input("What is your second favourite number? "))

#perform some simple math
add = number1 + number2 
multiply =  number1*number2 

#Greet the user and print the result
print(f"Hi {name}, here are some fun calculations with your favourite numbers:") 
print(f"{number1} + {number2} = {add}")
print(f" {number1} * {number2} = {multiply}")