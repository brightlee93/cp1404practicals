from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return super().__str__()

    def drive(self, distance):
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            distance_drive = super().drive(distance)
        else:
            distance_drive = 0
        return distance_drive

