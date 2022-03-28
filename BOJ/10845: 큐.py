import sys

N = int(sys.stdin.readline().strip())

Queue = []
for _ in range(N):
    order = sys.stdin.readline().strip().split()
    if order[0] == 'push':
        Queue.append(order[1])
    elif order [0] == 'pop':
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[0])
            Queue.remove(Queue[0])
    elif order[0] == 'size':
        print(len(Queue))
    elif order[0] == 'empty':
        if len(Queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(Queue) != 0:
            print(Queue[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(Queue) !=0:
            print(Queue[-1])
        else:
            print(-1)