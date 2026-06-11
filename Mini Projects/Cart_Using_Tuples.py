print("\nHi, Welcome to xyz Food and Beverages\n")
prices = {
    "Rice": 80,
    "Milk": 60,
    "Paneer": 120,
    "Eggs": 70,
    "Chicken": 250,
    "Apples": 90,
    "Cooking Oil": 180,
    "Bread": 55,
    "Cheese": 150,
    "Bananas": 65,
    "Curd": 75,
    "Butter": 110,
    "Jam": 85,
    "Coffee": 200,
    "Tea Powder": 95,
    "Almonds": 300,
    "Cashews": 350,
    "Honey": 160,
    "Cornflakes": 140,
    "Orange Juice": 130
}

user_data = []
item = None
while True:
    item = input("Kindly enter your item's name or press 'exit' to exit: ").strip()
    if item == 'exit':
        break
    if item not in prices:
        print("Sorry! Item is not available at the moment")
        continue
    quantity = int(input("Kindly enter your item's quantity: "))
    price = prices[item]
    user_data.append((item, price, quantity))


def add_price():
    tot_price = 0
    for i in user_data:
        tot_price+=(i[1])*(i[2])
    return tot_price


total_price = add_price()
if total_price > 1000:
    after_discount_price = (95/100)*total_price

print("\nHere's your receipt: \n\n")
print("Item, Price(per item), Quantity\n")
for x in user_data:
    print(f"{x[0]}, {x[1]}, {x[2]}")


print(f"\nTotal price: {total_price}")
if after_discount_price != 0:
    print("Discount applied: 5%")
    print(f"Grand Total: {after_discount_price}")