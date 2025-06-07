# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop: while loop for rows
while row < size:
    # Inner loop: for loop for columns (prints asterisks on the same line)
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
