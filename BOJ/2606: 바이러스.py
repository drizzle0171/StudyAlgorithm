import sys
input = sys.stdin.readline

n = int(input()) # 전체 컴퓨터 개수
v = int(input()) # 컴퓨터 쌍 개수
graph = [[] for i in range(n+1)] # 컴퓨터 개수만큼 2차원 배열 만들기 (0번 컴퓨터는 없음 -> 접근할 때 쉬우라고!)
visited = [0] * (n+1) # 방문한 컴퓨터인지 표시
for i in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)