import sys
from collections import Counter

word = sys.stdin.readline().strip()
alpha = [chr(i) for i in range(97, 123)]
word_key = list(Counter(word).keys())
word_value = list(Counter(word).values())
result = [0]*len(alpha)

for i in range(len(word_key)):
    index = alpha.index(word_key[i])
    result[index] = word_value[i]

for i in range(len(result)):
    print(result[i], end=" ")