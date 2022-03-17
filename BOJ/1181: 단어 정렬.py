# 길이가 짧은 것부터 ㅇ
# 길이가 같으면 사전 순으로 ㅇ
# 중복 불허 ㅇ

import sys
N = int(sys.stdin.readline())

words = []
for _ in range(N):
    words.append(sys.stdin.readline().strip())

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