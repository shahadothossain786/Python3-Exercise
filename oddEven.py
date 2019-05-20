#input a number from user and check odd or even
# A number is even if division by 2 give a reminder of 0
# If reminder is 1, it's odd

num = int(input("Give A Number : "))
if (num % 2) == 0:
    print("{0} is Even Number ". format(num))
else:
        print("{0} is Odd Number ". format(num))

