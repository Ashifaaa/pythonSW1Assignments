import random
# 1.
# class Elevator:
#     def __init__(self, bottom_floor, top_floor):
#         self.current_floor = bottom_floor
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#
#     def go_to_floor(self, target_floor):
#         if target_floor < self.bottom_floor or target_floor > self.top_floor:
#             print(f"Invalid floor number. Choose between {self.bottom_floor} and {self.top_floor}")
#             return
#
#         while self.current_floor != target_floor:
#             if self.current_floor < target_floor:
#                 self.floor_up()
#             else:
#                 self.floor_down()
#
#     def floor_up(self):
#         self.current_floor += 1
#         print(f"Elevator moved up to floor {self.current_floor}")
#
#     def floor_down(self):
#         self.current_floor -= 1
#         print(f"Elevator moved down to floor {self.current_floor}")
#
# elevator = Elevator(1, 10)
#
# elevator.go_to_floor(5)
#
# elevator.go_to_floor(1)

# # 2.
# class Elevator:
#     def __init__(self, bottom_floor, top_floor):
#         self.current_floor = bottom_floor
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#
#     def go_to_floor(self, target_floor):
#         if target_floor < self.bottom_floor or target_floor > self.top_floor:
#             print(f"Invalid floor number. Choose between {self.bottom_floor} and {self.top_floor}")
#             return
#
#         while self.current_floor != target_floor:
#             if self.current_floor < target_floor:
#                 self.floor_up()
#             else:
#                 self.floor_down()
#
#     def floor_up(self):
#         self.current_floor += 1
#         print(f"Elevator moved up to floor {self.current_floor}")
#
#     def floor_down(self):
#         self.current_floor -= 1
#         print(f"Elevator moved down to floor {self.current_floor}")
#
# class Building:
#     def __init__(self, bottom_floor, top_floor, num_elevators):
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#         self.num_elevators = num_elevators
#         self.elevators = []
#
#         elevator_counter = 0
#         while elevator_counter < num_elevators:
#             self.elevators.append(Elevator(bottom_floor, top_floor))
#             elevator_counter += 1
#
#     def run_elevator(self, elevator_number, destination_floor):
#         if 0 <= elevator_number < self.num_elevators:
#             elevator = self.elevators[elevator_number]
#             elevator.go_to_floor(destination_floor)
#         else:
#             print(f"Invalid elevator number. Choose between 0 and {self.num_elevators - 1}")
#
# bottom_floor = 1
# top_floor = 10
# num_elevators = 3
#
# building = Building(bottom_floor, top_floor, num_elevators)
#
# building.run_elevator(0, 5)
# building.run_elevator(1, 8)

# 3.
# class Elevator:
#     def __init__(self, bottom_floor, top_floor):
#         self.current_floor = bottom_floor
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#
#     def go_to_floor(self, target_floor):
#         if target_floor < self.bottom_floor or target_floor > self.top_floor:
#             print(f"Invalid floor number. Choose between {self.bottom_floor} and {self.top_floor}")
#             return
#
#         while self.current_floor != target_floor:
#             if self.current_floor < target_floor:
#                 self.floor_up()
#             else:
#                 self.floor_down()
#
#     def floor_up(self):
#         self.current_floor += 1
#         print(f"Elevator moved up to floor {self.current_floor}")
#
#     def floor_down(self):
#         self.current_floor -= 1
#         print(f"Elevator moved down to floor {self.current_floor}")
#
# class Building:
#     def __init__(self, bottom_floor, top_floor, num_elevators):
#         self.bottom_floor = bottom_floor
#         self.top_floor = top_floor
#         self.num_elevators = num_elevators
#         self.elevators = []
#
#         elevator_counter = 0
#         while elevator_counter < num_elevators:
#             self.elevators.append(Elevator(bottom_floor, top_floor))
#             elevator_counter += 1
#
#     def run_elevator(self, elevator_number, destination_floor):
#         if 0 <= elevator_number < self.num_elevators:
#             elevator = self.elevators[elevator_number]
#             elevator.go_to_floor(destination_floor)
#         else:
#             print(f"Invalid elevator number. Choose between 0 and {self.num_elevators - 1}")
#
#     def fire_alarm(self):
#         for elevator in self.elevators:
#             elevator.go_to_floor(self.bottom_floor)
#         print("Fire alarm activated!!!!!@All elevators moved to the bottom floor.")
#
#
# bottom_floor = 1
# top_floor = 10
# num_elevators = 3
#
# building = Building(bottom_floor, top_floor, num_elevators)
#
# building.run_elevator(0, 5)
# building.run_elevator(1, 8)
# building.fire_alarm()

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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print("{:<12} {:<15} {:<15} {:<20}".format("Car", "Max Speed (km/h)", "Distance (km)", "Current Speed (km/h)"))
        print("="*64)
        for car in self.cars:
            print("{:<12} {:<15} {:<15} {:<20}".format(car.registration_number, car.max_speed, car.travelled_distance, car.current_speed))

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

car_list = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car_list.append(Car(registration_number, max_speed))

grand_derby = Race("Grand Demolition Derby", 10000, car_list)

hour_counter = 0
under_race_dist = True
while under_race_dist:
    grand_derby.hour_passes()
    hour_counter += 1

    if hour_counter % 10 == 0:
        grand_derby.print_status()

    under_race_dist = not grand_derby.race_finished()

grand_derby.print_status()
print(f"\nRace finished in {hour_counter} hours.")