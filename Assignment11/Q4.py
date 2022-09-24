# 4. Write a python script to calculate sum of first N odd natural numbers

n = int(input("Enter a number : "))
odd_sum = 0
while n:
    odd_sum += n*2-1
    n -= 1
print('Sum of first n: ', odd_sum)
