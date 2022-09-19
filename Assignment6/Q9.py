# 9. Write a python script to check whether a given year is a leap year or not.

a = int(input("Enter year : "))
if a % 4 == 0:
    print(a, " is leap year ")
else:
    print(a, " is not leap year ")
