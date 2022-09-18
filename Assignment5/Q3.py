# 3. Write a python script to swap data of two variables

# x = 10
# y = 20
# print("X : ", x, "Y : ", y, end='\nAfter swapping \n')

# temp = x
# x = y
# y = temp
# print('X : ', x, 'Y : ', y)


x = int(input('Enter a number 1 : '))
y = int(input('Enter a number 2 : '))

print('X : ', x, ' Y : ', y, end=' \nAfter Swapping \n')

temp = x
x = y
y = temp

del temp

print('X : ', x, ' Y : ', y)
