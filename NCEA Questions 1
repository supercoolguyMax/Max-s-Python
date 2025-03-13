"""this code asks the user to input a battery charge, if the charge is equal to 1.2 then it will print beep otherwise it will print boop"""


#used to store all the numbers the user inputs
charge_list = []

#used 'try' to block any invalid inputs
#asks the user for an input

try:
    charge = float(input("Enter your input: "))
    while charge != -1:
        charge_list.append(charge)
        charge = float(input("Enter your input: "))
        if charge < -1:
            break


#

except ValueError:
    print("Not robot compliant")
#
for charge in charge_list:
    if charge >= 1.2:
        print("Beep")
    else:
        print("Boop")