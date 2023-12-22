# 1. Write a program that asks a fisher the length of a zander in centimeters
zander_length = float(input("Enter the length of zander in cm: "))
size_limit = 42
if zander_length >= size_limit:
    print("Zander can be kept! Goodjob!")
else:
    limit_difference = size_limit - zander_length
    print(f"Zander must be released. It's {limit_difference:.2f} cm below size limit")


# 2. Write a program that asks the user to enter the cabin class of a cruise ship and then prints out
# a written description according to the list below
cabin_class = input("Enter the cabin class (LUX, A, B, C): ")

if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")


# 3. Write a program that asks for the biological gender and hemoglobin value (g/l)
gender = input("Enter your biological gender (male/female): ")
hemoglobin_value = float(input("Enter your hemoglobin value in g/l: "))

normal_range_female = (117, 155)
normal_range_male = (134, 167)

if gender == "female":
    if normal_range_female[0] <= hemoglobin_value <= normal_range_female[1]:
        print("Your hemoglobin level is normal.")
    elif hemoglobin_value < normal_range_female[0]:
        print("Your hemoglobin level is low.")
    else:
        print("Your hemoglobin level is high.")
elif gender == "male":
    if normal_range_male[0] <= hemoglobin_value <= normal_range_male[1]:
        print("Your hemoglobin level is normal.")
    elif hemoglobin_value < normal_range_male[0]:
        print("Your hemoglobin level is low.")
    else:
        print("Your hemoglobin level is high.")
else:
    print("Invalid gender.")


# 4. Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
