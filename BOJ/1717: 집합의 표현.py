import sys
input = sys.stdin.readline

# n, m = map(int, input().split())
# n_list = [[i] for i in range(n+1)]

# for _ in range(m):
#     command, a, b = map(int, input().split())
#     if command==0:
#         n_list[a].extend(n_list[b])
#         n_list[a] = list(set(n_list[a]))
#         n_list[b].extend(n_list[a])
#         n_list[b] = list(set(n_list[b]))
#         for i in n_list[b]:
#            n_list[i].extend(n_list[b])
#            n_list[i] = list(set(n_list[a])) 
#     else:
#         if b in n_list[a]:
#             print("YES")
#         else:
#             print("NO")

# n, m = map(int, input().split())
# n_list = [i for i in range(n+1)]
# idx = [i for i in range(n+1)]

# for _ in range(m):
#     command = sorted(list(map(int, input().split())))
#     if command[0]==0:
#         n_list[command[2]] = n_list[min(idx[command[1]], n_list[command[1]])]
#     else:
#         if n_list[command[2]] == n_list[command[1]]:
#             print("YES")
#         else:
#             print("NO")

# n, m = map(int, input().split())
# n_list = []

# for _ in range(m):
#     command, a, b = (map(int, input().split()))
#     if command == 0:
#         for i in range(len(n_list)):
#             if a not in n_list[i] and b not in n_list[i]:
#                 n_list.append(set(a, b))
#     else:
#         for i in range(len(n_list)):
#             if a in n_list[i]:
#                 if b in n_list[i]:
#                     print("YES")
#                 else:
#                     print("NO")

sys.setrecursionlimit(100000)

n, m = map(int, input().split())
n_list = [i for i in range(n+1)]

def find(x):
    if n_list[x] == x:
        return x
    
    n_list[x] = find(n_list[x])
    return n_list[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        n_list[b] = a
    else:
        n_list[a] = b

for _ in range(m):
    command, a, b = map(int, input().split())
    if command==0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('yes')
        else:
            print('no!')