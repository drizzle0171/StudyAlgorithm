import sys
N = int(sys.stdin.readline())

words = set()
for _ in range(N):
    words.add(sys.stdin.readline().strip())

words = list(words)
words.sort(key=lambda x: (len(x), x))
# answer = set(words) - 실패
answer = []
for i in range(N):
    if words[i] in answer:
        continue
    else:
        answer.append(words[i])
for word in answer:
    print(word)