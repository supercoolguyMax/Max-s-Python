"""This code will ask the user for the temperature"""

temp_list = []

"""Asking the user for temperature"""

while True:
    try:
        temp = int(input("Enter the temperature: "))

        if temp == -1:
            break
        else:
             temp_list.append(temp)



    except ValueError:
        print("Invalid temperature.")
for temp in temp_list:
    if temp < 34:
        print("too cold")
    elif temp >= 34 and temp <= 42:
        print("just right")
    else:
        print("too hot")