# import sys
# input = sys.stdin.readline

# n = int(input())
# n1, n2 = map(int, input().split())
# m = int(input())
# graph = [[] for i in range(n+1)]
# visited = [0] * (n+1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# def dfs(k):
#     visited[k] = 1
#     for i in graph[k]:
#         if i == n1:
#             visited[i] = 1
#             return
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(i)

# dfs(n2)
# print(graph)
# print(visited)
# if visited[n1] == 1 and visited[n2] == 1:
#     print(sum(visited)-1)
# else:
#     print(-1)
    
# 입력값 받는 부분
N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = 0
####

# 어떤 노드들이 연결되어 있는지 graph라는 2차원 배열에 저장
for _ in range(M):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

# dfs
def dfs(v, num):
    global result  
    num += 1
    visited[v] = True

    if v == B:
        result += num

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

dfs(A, 0)

if result == 0:
  print(-1)
else:
  print(result-1)