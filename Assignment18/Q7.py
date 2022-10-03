# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'A': 110, 'B': 210, 'C': 310}
d3 = {'name': 'Naren', 'works_at': 'iNeuron'}

d4 = {1: d1, 2: d2, 3: d3}

print(d4)
