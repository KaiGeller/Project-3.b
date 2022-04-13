integer = int(input("Please enter a positive integer: "))
print("The factors of " + str(integer) + " are:")
for number in range(integer ,0,-1):
    if integer/number %1 == 0:
        print(int(integer/number))
1
