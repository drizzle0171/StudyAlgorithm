import sys
input = sys.stdin.readline

n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))

real = list(range(1, n+1))
score.sort()
result = 0

for i in range(n):
    result +=  abs(score[i]-real[i])
    
print(result)