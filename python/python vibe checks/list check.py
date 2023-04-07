food = ["Cheese", "Milk", "Bread", "Chicken Nuggets", "Grilled Cheese","Yogurt","Pancakes","Onion"]
print(food)
food.append("Paper")
print(len(food))
print(food)
Last = []
ef = "n"
while ef != "quit":
    ef = input("What's ur pet's name?\n")
    if ef != "quit":
        Last.append(ef)
Last.sort()
print(Last)