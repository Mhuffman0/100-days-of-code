import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
BASE_MAX_CAR_COUNT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.max_car_count = BASE_MAX_CAR_COUNT

    def create_car(self):
        if len(self.all_cars) < self.max_car_count and random.randint(1, 6) == 1:
            print(f"car added ({len(self.all_cars)})")
            car = Car(random.choice(COLORS))
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.move()

    def level_up(self):
        for car in self.all_cars:
            car.movement_speed += 0.25
        self.max_car_count += 1
