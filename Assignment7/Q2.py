# 2. Write a menu driven program to perform following operations - Addition, Subtraction,
# Multiplication, Division

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
print('\n1. Addition \n2. Subtraction \n3. Multiplication, \n4. Division')
c = int(input('\nSelect operation you want to do : '))

match c:
    case 1:
        print('Addition : ', num1+num2)
    case 2:
        print('Subtraction : ', num1-num2)
    case 3:
        print('Multiplication : ', num1*num2)
    case 4:
        print('Division : ', num1/num2)
