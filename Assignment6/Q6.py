# 6. Write a python script to check whether a given number is a three digit number or not.

a = int(input("Enter a num : "))
a = str(a)
if len(a) == 3:
    print(a, "is a three digit number")
else:
    print(a, "is not a three digit number")
