for i in range(-20,41,5):
    print(i, end = " ")
print()
for i in range(5):
    for j in range(2):
        print("*", end = " ")
    print()
n = 50
while n > 0:
    print(n)
    n -= 10
option = "yes"
cookie = 0
while option != "no":
    if option == "yes":
        print("here's a cookie")
        cookie += 1
    option = input("Would you like another cookie?\n")
print("You have", cookie, "cookies.")