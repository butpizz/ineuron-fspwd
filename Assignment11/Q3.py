# 3. Write a python script to calculate sum of cubes of first N natural numbers

n = int(input("Enter a number : "))
cubes = 0
while n:
    cubes += n**3
    n -= 1

print('Sum of squares : ', cubes)
