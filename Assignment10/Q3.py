# 3. Write a python script to print first M multiples of N.

n = int(input("Enter N number : "))
for i in range(1, int(input("How many multiples ? "))+1):
    print(n*i)
print()
