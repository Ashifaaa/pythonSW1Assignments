import random
# Write a program that asks your name and then greets you by your name
name = input("Enter name: ")
print(f"Hello, {name}!")

# Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
radius = int(input("Enter radius of circle: "))
area = 3.14159 * radius ** 2
print(f"Area of circle: {area}")

# Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides
length = int(input("Enter length: "))
width = int(input("Enter width: "))
perimeter = length * 4
area = length * width
print(f"Perimeter of the triangle: {perimeter}\nArea of the triangle: {area}")


# Write a program that asks the user for three integer numbers. The program prints out the sum, product,
# and average of the numbers.
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum/3

print(f"Sum: {sum}\nProduct: {product}\nAverage: {average}")


# Write a program that asks the user to enter a mass in medieval units: talents(leiviskä),pounds(naula),and lots(luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_pound = (talents * 20) + pounds
total_lots = (total_pound * 32) + lots
total_grams = total_lots * 13.3

kilograms = int(total_grams // 1000)
grams = (total_grams % 1000)

print(f"The weight in modern units:\n{kilograms} kilograms and {grams:.2f} grams.")


# Write a program that draws two random combinations of numbers for a combination lock
digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)
three_digit_combo = [digit1, digit2, digit3]

digit4 = random.randint(1, 6)
digit5 = random.randint(1, 6)
digit6 = random.randint(1, 6)
digit7 = random.randint(1, 6)
four_digit_combo = [digit4, digit5, digit6, digit7]

print(f"Random 3-digit code: {three_digit_combo}\nRandom 4-digit code: {four_digit_combo}")
