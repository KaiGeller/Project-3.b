integer = int(input("Please enter a positive integer: "))
print("The factors of " + str(integer) + " are")
for number in range(integer + 1):
    if number > 0 and integer/number %1 == 0:
        print(str(integer/number))
