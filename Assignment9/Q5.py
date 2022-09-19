# 5. Write a python script to print first 10 odd natural numbers in reverse order

i = int(input('Enter a number : '))
while i:
    print(i*2-1, end=' ')
    i -= 1
