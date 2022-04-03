
def calculate_area(height, b1,b2):
    # Note that this function will only work for squares and rectangles
    area =0.5*height*(b1+b2)
    return area

print("This program will calculate the area for a trapazoid")
h = input("Please enter the height: ")
height = float(h)
b1 = input("Please enter the value of b1: ")
b1 = float(b1)
b2 = input("Please enter the value of b2: ")
b2 = float(b2)

area = calculate_area(height, b1,b2)
print("The area is: " + str(area))

