from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


    current_taxi = None
    bill_balance = 0

    print("Let's drive!")
    menu_selection = input("q)uit, c)hoose taxi, d)rive \n").lower()
    while menu_selection != "q":
        if menu_selection == "c":
            taxi_entry_number = 0
            print("Taxis available:")
            for i in taxis:
                print(taxi_entry_number, "-", i)
                taxi_entry_number += 1
            taxi_selection = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_selection]
            current_bill = current_taxi.get_fare()
            bill_balance += current_bill
            print("Bill to date: ${:.2f}".format(bill_balance))
            menu_selection = input("q)uit, c)hoose taxi, d)rive \n").lower()
        elif menu_selection == "d":
            current_distance = current_taxi.drive(int(input("Driven how far? ")))
            current_bill = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_bill))
            bill_balance += current_bill
            print("Bill to date: ${:.2f}".format(bill_balance))
            menu_selection = input("q)uit, c)hoose taxi, d)rive \n").lower()
        else:
            print("invalid option")
            menu_selection = input("q)uit, c)hoose taxi, d)rive \n").lower()
    print("Total trip cost: ${:.2f}".format(bill_balance))
    print("Taxis are now")
    taxi_entry_number = 0
    for i in taxis:
        print(taxi_entry_number, "-", i)
        taxi_entry_number += 1



main()
