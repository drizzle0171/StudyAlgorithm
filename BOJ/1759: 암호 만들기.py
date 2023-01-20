import sys
input = sys.stdin.readline

l, c = map(int, input().split())
char = list(map(str, input().split()))
char = sorted(char)

answer = []
result = []

def consonant(string):
    dict = {'a':0, 'b':1, 'c':1, 'd':1, 'e':0, 'f':1, 'g':1, 'h':1, 
            'i':0, 'j':1, 'k':1, 'l':1, 'm':1, 'n':1, 'o':0,
            'p':1, 'q':1, 'r':1, 's':1, 't':1, 'u':0, 'v':1, 
            'w':1, 'x':1, 'y':1, 'z':1}
    total = 0
    for i in range(len(string)):
        total += dict[string[i]]
    return total

def collection(string):
    dict = {'a':1, 'b':0, 'c':0, 'd':0, 'e':1, 'f':0, 'g':0, 'h':0, 
            'i':1, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':1,
            'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':1, 'v':0, 
            'w':0, 'x':0, 'y':0, 'z':0}
    total = 0
    for i in range(len(string)):
        total += dict[string[i]]
    return total

def dfs(start):
    if len(result) == l:
        if (consonant(result) >=2):
            if (collection(result) >=1):
                answer.append(''.join(result))
                return


    for i in range(start, len(char)):
        if char[i] not in result:
            result.append(char[i])
            dfs(i+1)
            result.pop()

dfs(0)
for i in answer:
    print(i)