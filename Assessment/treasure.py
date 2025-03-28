# treasure variable
treasure_coords = []

# running x input
while True:
    x_input = input("Enter X coordinate: ")
    # breaking x input
    if x_input.lower() == "complete":
        break
    # invalid input handling for X coordinate
    try:
        x = int(x_input)
    except ValueError:
        print("Error. Invalid input. Please enter an integer.")
        continue
    
    # running y input
    y_input = input("Enter Y coordinate: ")
    # invalid input handling for Y coordinate
    try:
        y = int(y_input)
    except ValueError:
        print("Error. Invalid input. Please enter an integer.")
        continue
    
    # adding valid x and y inputs if their sum is 10
    if x + y == 10:
        treasure_coords.append([x, y])

# printing coordinates
if treasure_coords:
    print("Treasure located at")
    for coord in treasure_coords:
        print(f"({coord[0]}, {coord[1]})")