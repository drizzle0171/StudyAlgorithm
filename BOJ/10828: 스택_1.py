import sys

N = int(sys.stdin.readline())
stack = []
cnt = 0

while True:
    order = sys.stdin.readline()
    if 'push' in order:
        order_list = order.split()
        stack.append(int(order_list[1]))
    elif 'pop' in order:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif 'size' in order:
        print(len(stack))
    elif 'empty' in order:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    cnt += 1
    if cnt==N:
        break