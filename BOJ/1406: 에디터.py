import sys

string = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline())

loc = len(string)
present_loc = loc

for _ in range(N):
    order = sys.stdin.readline().strip().split()
    if order[0] == 'L': # 뒤로 가기
        if present_loc == 0:
            continue
        else:
            present_loc -=1
    elif order [0] == 'D': # 앞으로 가기
        if present_loc == loc:
            continue
        else:
            present_loc += 1
    elif order [0] == 'B': # 왼쪽에 있던 문자 삭제
        if present_loc == 0:
            continue
        else:
            string.remove(string[present_loc-1])
            present_loc-=1
    else:
        if present_loc == loc: ## 예제 1을 위해서 이걸 고쳐야 함
            string.append(order[1])
            present_loc+=1
        else: 
            string.insert(present_loc, order[1]) #loc 왼쪽에 추가함
            present_loc+=1
    loc = len(string)

for str in string:
    print(str, end='')