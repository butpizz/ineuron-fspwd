# 2. Write a python script to calculate sum of squares of first N natural numbers

n = int(input("Enter a number : "))
square = 0
while n:
    square += n**2
    n -= 1

print('Sum of squares : ', square)
