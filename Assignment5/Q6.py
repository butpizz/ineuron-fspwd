# 6. Write a python script which takes a three digit number from the user and displays
# only its middle digit.

x = int(input("Enter 3 digit num : "))
x = x//10
x = x % 10
print(x)
