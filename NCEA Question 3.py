transactions = []

#variables 

STOP = 0
BALANCE = 200

#asking the user for input

while True:
    try:
        transaction = int(input("Enter the amount spent: "))
        if transaction == STOP:
            break
        if transaction < 0:
            print("That is not a valid transaction.")
            continue
        BALANCE -= transaction
        transactions.append(BALANCE)
        if BALANCE <= 0:
            break
    except ValueError:
        print("That is not a valid transaction.")
#
print("My bank balances have been:")
for balance in transactions:
    print(balance)