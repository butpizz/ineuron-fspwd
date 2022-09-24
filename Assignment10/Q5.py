# 5. Write a python script to print table of user’s choice

n = int(input("Enter a number : "))
for i in range(1, int(input("How many multiples ? "))+1):
    print(n, "x", i, "=", n*i)
print()
