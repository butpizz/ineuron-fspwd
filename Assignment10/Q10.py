# 10. Write a python script to display all prime numbers within a range.
# range
# start = 15
# end = 45

l = 15
h = 45
for num in range(l, h):
    if(num > 1):
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num, end='  ')
