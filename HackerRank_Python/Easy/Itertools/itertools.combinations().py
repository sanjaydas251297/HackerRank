from itertools import combinations
word, num = input().split(" ")
for l in range(1,int(num)+1):
    for c in combinations (sorted(word),l):
        print(''.join(c))