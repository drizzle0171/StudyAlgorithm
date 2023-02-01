import sys
input = sys.stdin.readline

n = input()
m = int(input())
if m:
    broken = list(map(int, input().split()))
elif n == 100:
    print(0)
else:
    print(len(n))

current = 100
button = list(range(9))
cnt = 0

for i in broken:
    button[i] = 'n'

channel = []
k = 0
while(len(channel) != len(n)):
    if button[n[k]] != 'n':
        channel.append(button[n[k]])
    else:
        