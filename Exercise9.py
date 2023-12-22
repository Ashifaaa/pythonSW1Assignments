import random
# 1.
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

new_car = Car("ABC-123","142km/h")
print(f"Registration number: {new_car.registration_number}\nMaximum speed: {new_car.max_speed}\nCurrent speed: {new_car.current_speed}\nTravelled distance: {new_car.travelled_distance}")


# 2.
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        # Ensure speed stays within bounds (0 to max_speed)
        self.current_speed = self.current_speed + speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

new_car = Car("ABC-123",142)

new_car.accelerate(30)
print(f"Current speed after +30 km/h: {new_car.current_speed}km/h")

new_car.accelerate(70)
print(f"Current speed after +70 km/h: {new_car.current_speed}km/h")

new_car.accelerate(50)
print(f"Current speed after +50 km/h: {new_car.current_speed}km/h")

new_car.accelerate(-200)
print(f"Current speed after -200 km/h: {new_car.current_speed}km/h")

# 3.
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        # Ensure speed stays within bounds (0 to max_speed)
        self.current_speed = self.current_speed + speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled


new_car = Car("ABC-123",142)

new_car.accelerate(30)
print(f"Current speed after +30 km/h: {new_car.current_speed}km/h")

new_car.drive(1.5)
print(f"Travelled distance after driving for 1.5 hours: {new_car.travelled_distance} km")

new_car.accelerate(70)
print(f"Current speed after +70 km/h: {new_car.current_speed}km/h")

new_car.drive(2)
print(f"Travelled Distance after driving for 2 hours: {new_car.travelled_distance}km")

# 4.
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        # Ensure speed stays within bounds (0 to max_speed)
        self.current_speed = self.current_speed + speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled

car_list = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car_list.append(Car(registration_number, max_speed))

race_distance = 10000
hour_counter = 0
under_race_dist = True
while under_race_dist:
    for car in car_list:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.travelled_distance >= race_distance:
            under_race_dist = False
            break
    hour_counter += 1

print("Car Race Results:")
print("{:<12} {:<15} {:<15} {:<20}".format("Car", "Max Speed (km/h)", "Distance (km)", "Current Speed (km/h)"))
print("="*64)
for car in car_list:
    print("{:<12} {:<15} {:<15} {:<20}".format(car.registration_number, car.max_speed, car.travelled_distance, car.current_speed))

print("\nRace finished in", hour_counter, "hours.")