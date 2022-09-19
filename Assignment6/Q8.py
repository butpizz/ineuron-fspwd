# 8. Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots

a = int(input("Enter a num1 : "))
b = int(input("Enter a num2 : "))
c = int(input("Enter a num3 : "))

root = (b**2)-(4*a*c)

if root > 0:
    print("Given quadratic equation has real & distinct")
elif root == 0:
    print("Given quadratic equation has two real & equal")
else:
    print("Given quadratic equation has two real & imaginary")
