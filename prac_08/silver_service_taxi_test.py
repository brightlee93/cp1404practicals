from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    print("{:.2f}".format(hummer.get_fare()))



main()
