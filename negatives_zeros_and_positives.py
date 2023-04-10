negatives_list = []
zero_list = []
positive_list = []

more_numbers = True
while more_numbers:
    number = input("Please type in a number or type in a blank line to stop: ")
    if number == " ":
        more_numbers = False
    else:
        number = int(number)
        if number < 0:
            negatives_list.append(number)
        if number == 0:
            zero_list.append(number)
        if number > 0:
            positive_list.append(number)


print(negatives_list)
for i in range (0, len(negatives_list)):
    print(negatives_list[i])

print(zero_list)
for i in range (0, len(zero_list)):
    print(zero_list[i])

print(positive_list)
for i in range (0, len(positive_list)):
    print(positive_list[i])