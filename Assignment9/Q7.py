# 7. Write a python script to print first N even natural numbers in reverse order
i = int(input('Enter a number : '))
while i:
    print(i*2, end=' ')
    i -= 1
