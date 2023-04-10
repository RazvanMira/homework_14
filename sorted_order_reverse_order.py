lst = []

while True:
    number = int(input("Please type in a number or type in 0 to stop: "))
    if number != 0:
        lst.append(number)
    elif number == 0:
        break

print("Initial list is:", lst)
for i in range (0, len(lst)):
    print(lst[i])

print("---")
lst.sort()
for i in range (0, len(lst)):
    print(lst[i])

print("---")
lst.reverse()
for i in range (0, len(lst)):
    print(lst[i])