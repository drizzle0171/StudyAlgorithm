import sys

word = sys.stdin.readline().strip()
alpha = [chr(i) for i in range(97, 123)]
result = []

for i in range(len(alpha)):
    result.append(word.count(alpha[i]))

for i in range(len(result)):
    print(result[i], end=" ")