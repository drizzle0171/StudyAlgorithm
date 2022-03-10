import sys

n = sys.stdin.readline()
n_list = list(n)
n_list.sort(reverse=True)

for i in n_list:
    print(i, end="")
