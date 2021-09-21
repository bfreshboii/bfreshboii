# LAB 1 - THE PAINT SHOP
# Code a Python program that calculates the amount of paint you need to cover the walls in your family room. 
# The salesperson at the home improvement store told you to buy 1 gallon of paint for every 150 square feet of 
# wall you need to paint.

# Assuming that the room is rectangular in shape, the program should take in as input the width of your 
# two sets of walls and the height of the room.

# The program should output the number of gallons required to paint the room. 
# Paint is sold only by the gallon.

#Purpose/Concepts: Input and output to screen, string concatentation, datatype casting, simple math operations

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
        print("This Program Will Calculate How Much Gallons Of Paint Needed To Paint The Room")

    #this is where i declare my variables
        firstWidth = input("What is the width of the longer parallel set of walls in square feet?:")
        secondWidth = input("What is the width of the shorter parallel set of walls in square feet?:")
        roomHeight = input("What is the height of the room in square feet?:")
        multiple = int(2) #This number 2 is for the program to calculate the formula for the perimeter 2(p+l)
        sqaureFeet = int(150) #declaring the 150 sqaurefeet as an int

    #This is where my calculations are done
        perimeter = (int(firstWidth) + int(secondWidth)) * multiple #This line is calculating the perimeter of the rectangle
        wallArea = perimeter * int(roomHeight) #This line is calculating the size of the wall area
        oneGallonofPaint = wallArea / sqaureFeet #dividing wall area by the square feet to determine how much gallons of paint i will need

        print("You will need", oneGallonofPaint, "gallons of paint for your room!")


    # YOUR CODE ENDS HERE

main()