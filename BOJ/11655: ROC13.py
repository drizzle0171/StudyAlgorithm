import sys

string = list(sys.stdin.readline().rstrip())
answer = []

# 대문자: 65~90
# 소문자: 97~122

for i in string:
    alpha = ord(i)
    if (65<=alpha<=90):
        new = alpha+13
        if (new) > 90:
            new -= 26
        answer.append(chr(new))
        new = 0    
    elif (97<=alpha<=122):
        new = ord(i)+13
        if (new) > 122:
            new-= 26
        answer.append(chr(new))
        new = 0
    else:
        answer.append(i)
    
for i in answer:
    print(i, end='')
    