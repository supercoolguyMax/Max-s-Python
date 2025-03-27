"""This code will ask for coordinates that will be used to locate a treasure. The coordinates will be used to determine if the treasure is located at the coordinates entered."""
while True:
    x_input = input("Enter X coordinate: ")
    if x_input == "complete":
        break
    y_input = input("Enter Y coordinate: ")
    if not x_input.isdigit() or not y_input.isdigit():
        print("Error. Invalid.")
        continue
    x = int(x_input)
    y = int(y_input)
    if x + y == 10:
        print("Treasure located at ({}, {})".format(x, y))

print{'')}
