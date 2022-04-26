import sys

order = int(sys.stdin.readline())
deque =[]

for _ in range(order):
    command = sys.stdin.readline().strip().split()
    if command[0]== 'push_front':
        deque.insert(0, command[1])
    elif command[0] == 'push_back':
        deque.append(command[1])
    elif command[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif command[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(-1))
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(deque) !=0:
            print(deque[-1])
        else:
            print(-1)

# insert (-1, command[1]) -> append로 바꾸니까 맞았음