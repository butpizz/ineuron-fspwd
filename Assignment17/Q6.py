# 6. Write a python program to add elements of list to a set thisset = {"Python", "Django", "JavaScript"} mylist = ["Java", "C"]

s = {"Python", "Django", "JavaScript"}
l = ["Java", "C"]

s.update(l)
print(s)
