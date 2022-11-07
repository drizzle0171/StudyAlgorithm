import sys
input = sys.stdin.readline

string = list(map(str, input().rstrip()))
result = set()

for i in range(len(string)):
    for j in range(len(string)+1):
        if string[i:j]:
            result.add("".join(string[i:j]))

print(string,result)
print(len(result))