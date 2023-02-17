import sys
input = sys.stdin.readline

n = int(input())
rope_w = []
maxWeight = 0
for _ in range(n):
    rope_w.append(int(input())) 
rope_w = sorted(rope_w)

for i in range(len(rope_w)-1, -1, -1):
    maxWeight = max(maxWeight, rope_w[i]*len(rope_w[i:]))

print(maxWeight)
