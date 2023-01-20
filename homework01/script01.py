#Anna Victoria Lavelle
#AVL578
#1/20/2023
#script01.py

words = []

with open('/home/avlav/words', 'r') as f:
    words = f.read().splitlines()

words.sort(key = len, reverse = True)

#print(words[:5])

for i in range(5):
    print(words[i])
