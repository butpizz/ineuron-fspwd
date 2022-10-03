# 10. Write a python program to get the key of lowest value from the dictionary.
# sample_dict = {
# 'C': 92,
# 'Java': 66,
# 'Python': 85
# }

# 1
sample_dict = {'C': 92, 'Java': 66, 'Python': 85}
print(min(sample_dict.values()))

# 2
value = min(sample_dict.values())
for k, v in sample_dict.items():
    if v == value:
        print(k, "has minimum value", v)
        break
