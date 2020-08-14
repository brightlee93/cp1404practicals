item_quantity = int(input("Number of items: "))
while item_quantity < 1:
    print("Invalid number of items!")
    item_quantity = int(input("Number of items: "))
subtotal_price = 0
for i in range(item_quantity):
    item_price = float(input("Price of item: "))
    subtotal_price = subtotal_price + item_price
if subtotal_price >= 100:
    total_price = subtotal_price * 0.9
print("Total price for {} items is ${:.2f}".format(item_quantity, total_price))
