# 10. Write a python script to print greater among three numbers. Print number only once
# even if the numbers are the same.

a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))

if a >= b and a >= c:
    print(a, "is greater")
elif b >= c and b > a:
    print(b, "is greater")
else:
    print(c, "is greater")


# if a > b:
#     if a > c:
#         print(a, 'is greater')
#     else:
#         print(c, 'is greater')
# else:
#     if b > c:
#         print(b, 'is greater')
#     else:
#         print(c, 'is greater')
