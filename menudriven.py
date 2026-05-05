def square(side):
	return side * side


def rectangle(length, breadth):
	return length * breadth


def circle(diameter):
	radius = diameter / 2
	return 3.14 * radius * radius


def triangle(base, height):
	return 0.5 * base * height


while True:
	print("\nMenu")
	print("1. Square")
	print("2. Rectangle")
	print("3. Circle")
	print("4. Triangle")
	print("5. Exit")

	choice = int(input("Enter your choice: "))

	if choice == 1:
		side = float(input("Enter side: "))
		print("Area of square =", square(side))
	elif choice == 2:
		length = float(input("Enter length: "))
		breadth = float(input("Enter breadth: "))
		print("Area of rectangle =", rectangle(length, breadth))
	elif choice == 3:
		diameter = float(input("Enter diameter: "))
		print("Area of circle =", circle(diameter))
	elif choice == 4:
		base = float(input("Enter base: "))
		height = float(input("Enter height: "))
		print("Area of triangle =", triangle(base, height))
	elif choice == 5:
		print("Exiting program")
		break
	else:
		print("Invalid choice, try again")
3