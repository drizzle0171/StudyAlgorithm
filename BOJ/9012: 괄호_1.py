import sys

N = int(sys.stdin.readline())
right = 0
left = 0
result = ''
for _ in range(N):
    input = list(sys.stdin.readline().strip())
    # for i in range(1,len(input)):
        # if (input[i-1]==right) and (input[i]==left):
        #     input[i-1], input[i] = 'True', 'True'
    for i in range(len(input)):
        if input[i] == '(':
            right += 1
        else:
            left += 1
        if left > right:
            result = 'NO'
    if (result == ''):
        if (left == right):
            result = 'YES'
        else:
            result = 'NO'
    right, left = 0, 0
    print(result)
    result = ''

    # right, left를 전체가 다 돌고도 확인을 해야 하는데 이미 0으로 초기화 시켜서 못함
    # 위에서 right == left 를 하자니 input 돌 때마다 해서 안됨