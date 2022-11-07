total = int(input())
N = int(input())

item = list()
for _ in range(N):
    item.append(list(map(int, input().split())))

total_item = 0
for i in range(N):
    total_item += item[i][0] * item[i][1]

if total_item == total:
    print("Yes")
else:
    print("No")