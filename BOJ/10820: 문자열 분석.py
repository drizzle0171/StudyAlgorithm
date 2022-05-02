import sys

while True:
    string = list(sys.stdin.readline().rstrip('\n'))
    lower, upper, num, space = 0, 0, 0, 0

    if not string:
        break
    for i in string:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
        elif i.isdigit():
            num+=1
        elif i == ' ':
            space+=1
    
    print(f'{lower} {upper} {num} {space}')
