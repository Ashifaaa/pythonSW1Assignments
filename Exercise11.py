import random
# # 1.
# class Publication:
#     def __init__(self, name):
#         self.name = name
#
#     def print_information(self):
#         print(f"Publication Name: {self.name}")
#
#
# class Book(Publication):
#     def __init__(self, name, author, page_count):
#         super().__init__(name)
#         self.author = author
#         self.page_count = page_count
#
#     def print_information(self):
#         super().print_information()
#         print(f"Author: {self.author}")
#         print(f"Page Count: {self.page_count}")
#
#
# class Magazine(Publication):
#     def __init__(self, name, chief_editor):
#         super().__init__(name)
#         self.chief_editor = chief_editor
#
#     def print_information(self):
#         super().print_information()
#         print(f"Chief Editor: {self.chief_editor}")
#
#
# donald_duck_magazine = Magazine("Donald Duck", "Aki Hyyppä")
# compartment_no_6_book = Book("Compartment No. 6","Rosa Liksom", 192)
#
# donald_duck_magazine.print_information()
# compartment_no_6_book.print_information()

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

    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

electric_car = ElectricCar("ABC-15", 180, 52.5)

gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(20)
gasoline_car.accelerate(15)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric Car Distance: {electric_car.travelled_distance} km")
print(f"Gasoline Car Distance: {gasoline_car.travelled_distance} km")


