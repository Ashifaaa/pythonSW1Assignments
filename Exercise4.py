# 1.Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
counter = 1
while counter <= 1000:
    if counter % 3 == 0:
        print(counter)
    counter += 1

# 2. Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
inches = float(input("Enter a length in inches (or a negative value to end): "))
while inches >= 0:
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters")

    inches = float(input("Enter another length in inches (or a negative value to end): "))

print("Goodbye.")


# 3. Write a program that asks the user to enter numbers until they enter an empty string to quit


