import sys
input = sys.stdin.readline

a, b = map(str, input().split())
b = list(b) # b 리스트화
len_a = len(a) # a 길이
max_cnt = 0
while len_a <=len(b): 
    cnt = 0
    for i in range(len_a): 
        if a[i] == b[i]:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
    del b[0]
print((len_a - max_cnt))

# a, b = map(str, input().split())
# if len(a) != len(b):
#     if a in b:
#         a = b
#     elif a[-1] == b[-1]:
#         a = b[:len(b)-len(a)] + a
#     elif a[0] == b[0]:
#         a = a + b[len(a):]
#     else:
#         for i in range(len(a)):
#             if a[i] in b:
#                 a = b[:b.index(a[i])]+a+b[len(b)-len(a):]
#                 break

# count = 0
# for i in range(len(a)):
#     if b[i] != a[i]:
#         count += 1
        
# print(count)

# 앞이 동일 ㅇ
# 뒤가 동일 ㅇ
# 사이가 동일 ㅇ
# 사이에 일부가 동일 ㅇ
# 모두 불일치 ㅇ