"""This program will check to see if the user has entered a valid integer in a specific range of values"""


# use contants for low and high value 
LOW = 1
HIGH = 10

# ask the user to type in a number
num = input('Please enter an integer: ')

# check to see if the number is valid 
if num.lstrip("-").isnumeric():
    num = int(num)
    if num < LOW:
        print(f'{num} is lower than {LOW}')
    elif num > HIGH: 
        print(f'{num} is greater than {HIGH}')
    else:
        print(f'Your number is {num}')
else:
    print(f'{num} is not an integer') 