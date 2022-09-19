# 10. Write a python script to print first 10 multiples of n

i = int(input('Enter a number : '))
x = 1
while x <= 10:
    print(i, 'X', x, '=', i*x)
    x += 1
