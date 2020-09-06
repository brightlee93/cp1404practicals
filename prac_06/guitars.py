from prac_06.guitar import Guitar

guitars = []
counter = 1
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_entry = Guitar(name, year, cost)
    print(guitar_entry, "added.")
    guitars.append(guitar_entry)
    name = input("Name: ")
# guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("These are my guitars")
for entry, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print("Guitar {0}: {guitar.name:20} ({guitar.year}), worth ${guitar.cost:10,.2f}{1}".format(entry, vintage_string,
                                                                                                guitar=guitar))
