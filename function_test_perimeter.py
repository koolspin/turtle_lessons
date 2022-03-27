
def calculate_perimeter(height, width):
    # Note that this function will only work for squares and rectangles
    perimeter = 2 * height + 2 * width
    return perimeter

print("This program will calculate the perimeter for a square or rectangle")
h = input("Please enter the height: ")
height = int(h)
w = input("Please enter the width: ")
width = int(w)
perim = calculate_perimeter(height, width)
print("The perimeter is: " + str(perim))

