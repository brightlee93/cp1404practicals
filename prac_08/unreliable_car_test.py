from prac_08.unreliable_car import UnreliableCar


def main():
    new_car = UnreliableCar("car1", 100, 10)
    new_car.drive(20)
    print(new_car)


main()
