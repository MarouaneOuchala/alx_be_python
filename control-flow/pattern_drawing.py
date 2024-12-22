# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to draw the rows of the pattern
while row < size:
    # Use a for loop to draw the columns in the current row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after completing a row
    print()
    row += 1
