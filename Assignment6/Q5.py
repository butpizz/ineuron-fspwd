# 5. Write a python script to print two given words in dictionary order

w1 = input("Enter word1 : ")
w2 = input("Enter word2 : ")

if w1 < w2:
    print(w1, w2, sep=' ')
else:
    print(w2, w1, sep=' ')
