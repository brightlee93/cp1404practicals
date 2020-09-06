from prac_06.guitar import Guitar

gibson_l5_ces = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013)
print("{} get.age() - Expect {}. Got {}".format(gibson_l5_ces.name, 98, gibson_l5_ces.get_age()))
print("{} get.age() - Expect {}. Got {}".format(another_guitar.name, 7, another_guitar.get_age()))
print("{} is_vintage() - Expect {}. Got {}".format(gibson_l5_ces.name, True, gibson_l5_ces.is_vintage()))
print("{} is_vintage() - Expect {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))



