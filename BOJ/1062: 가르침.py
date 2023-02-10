# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n, k = map(int, input().split()) #
# words = list() #
# char = set() #
# for _ in range(n): #
#     word = input().rstrip() #
#     words.append(word[4:-4]) #
#     for i in word[4:-4]:
#         char.add(i)

# char = list(char)
# already = ['a', 't', 'n', 'i', 'c']

# k -= 5
# if k <= 0:
#     print(0)

# else:
#     answer = n
#     maxCount = 0 
#     for comb in combinations(char, k):
#         candidate = set(already)
#         for i in comb:
#             candidate.add(i)
#         answer = n
#         minCount = 0
#         for word in words:
#             for i in word:
#                 if i not in candidate:
#                     answer -= 1
#                     break
#         maxCount = max(maxCount, answer)
#     print(maxCount)

# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n, k = map(int, input().split()) #
# alphabet = [1, 0, 1, 0, 0,
#             0, 0, 0, 1, 0,
#             0, 0, 0, 1, 0,
#             0, 0, 0, 0, 1,
#             0, 0, 0, 0, 0,
#             0]
# position = []
# words = list() #
# for _ in range(n): #
#     word = input().rstrip()[4:-4] #
#     for i in word:
#         alphabet[ord(i)-97] = 1
#         if (ord(i)-97) not in [0,2,8,13,19]:
#             position.append(ord(i)-97)

# k -= 5
# if k <= 0:
#     print(0)

# else:
#     answer = n
#     maxCount = 0 
#     for comb in combinations(position, k):
#         answer = n
#         minCount = 0
#         for word in words:
#             for i in word:
#                 if i not in candidate:
#                     answer -= 1
#                     break
#         maxCount = max(maxCount, answer)
#     print(maxCount)

import sys

n, k = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

# 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1


def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        answer = max(answer, readcnt)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


dfs(0, 0)
print(answer)

