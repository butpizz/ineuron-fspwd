# 7. Write a python script to check whether a given number is positive, negative or zero.

a = int(input("Enter a num : "))
if a > 0:
    print(a, "positive")
elif a == 0:
    print("It is zero")
else:
    print(a, "non-positive")
