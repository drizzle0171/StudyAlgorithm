import sys

n = sys.stdin.readline()
n_list = list(n)

n_list.sort(reverse=True)
n_to_str = [str(i) for i in n_list]
print(''.join(n_to_str))
