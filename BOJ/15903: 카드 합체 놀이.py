import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int, input().split()))
heap = []

for i in nlist:
    heapq.heappush(heap, i)
    
for _ in range(m):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap, x+y)
    heapq.heappush(heap, x+y)    

print(sum(heap))

# x = heapq.heappop(heap)
# y = heapq.heappop(heap)
# heapq.heappush(heap, x+y)
# heapq.heappush(heap, x+y)