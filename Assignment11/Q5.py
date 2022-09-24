# 5. Write a python script to calculate sum of first N even natural numbers

n = int(input("Enter a number : "))
even_sum = 0
while n:
    even_sum += n*2
    n -= 1
print('Sum of first n: ', even_sum)
