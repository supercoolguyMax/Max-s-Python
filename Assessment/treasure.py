"""This code will ask for coordinates that will be used to locate a treasure. The coordinates will be used to determine if the treasure is located at the coordinates entered."""
#treasure list
treasue_coords = []

#running x input

while True:
    x_input = input("Enter X coordinates: ")

#stopping the code when user inputs complete
    
    if x_input.lower == 'complete':
        break
#ouputing invaild numbers 
    try:
        x = int(x_input)
    except ValueError:
        print("Error. Invalid.")
        continue

#running y input
    try:
        y_input = input("Enter Y coordinates: ")
        y = int(y_input)
    except ValueError
        print("Error. Invalid.")
        continue

#adding the x input and the y input for final results 
    if y + x == 10:   
        treasue_coords.append((x, y))

    if treasue_coords:
        print("Treasure located at")
        for coord in treasure_coords 
            print(f"({coord{0}}), ({coord{1}})")
