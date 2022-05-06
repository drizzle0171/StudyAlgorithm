import sys

string = sys.stdin.readline().rstrip('\n')
answer = []

for i in range(len(string)):
    answer.append(string[i:])

answer.sort()

for i in answer:
    print(i, end="\n")