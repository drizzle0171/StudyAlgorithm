import sys

string = sys.stdin.readline().strip().split()

for i in range(len(string)):
    for j in reversed(range(len(string[i]))):
        