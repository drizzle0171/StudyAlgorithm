import sys
N = int(sys.stdin.readline())

words = set()
for _ in range(N):
    words.add(sys.stdin.readline().strip())

words = list(words)
words.sort(key = len)

for word in words:
    print(word)