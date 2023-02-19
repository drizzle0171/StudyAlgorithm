import sys
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

if len(num) == 1:
    print(num[0])
else:
    num.sort()
    total = [num[0]] + [0]*(n-1)
    for i in range(1, n):
        total[i] = total[i-1] + num[i]
    print(total)
    print(sum(total[1:]))

# import sys, heapq

# N = int(sys.stdin.readline())
# cards = [int(sys.stdin.readline()) for i in range(N)]
# heapq.heapify(cards)
# cnt = 0

# while len(cards) > 1:
#     tmp = heapq.heappop(cards) + heapq.heappop(cards)
#     heapq.heappush(cards, tmp)
#     cnt += tmp
    
# print(cnt)