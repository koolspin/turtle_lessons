
def calculate_area(height, width):
    # Note that this function will only work for squares and rectangles
    area = height *  width
    return area

print("This program will calculate the area for a square or rectangle")
h = input("Please enter the height: ")
height = int(h)
w = input("Please enter the width: ")
width = int(w)
perim = calculate_area(height, width)
print("The area is: " + str(perim))

