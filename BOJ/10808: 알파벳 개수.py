import sys
from collections import Counter

word = sys.stdin.readline().strip()
word_key = list(Counter(word).keys())
word_value = list(Counter(word).values())
result = [0]*26

for i in range(len(word_key)):
    index = ord(word_key[i])-97
    result[index] = word_value[i]

for i in range(len(result)):
    print(result[i], end=" ")