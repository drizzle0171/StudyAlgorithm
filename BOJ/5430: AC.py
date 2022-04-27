TestNum = int(input())

for i in range(TestNum):
    Orders = list(input())
    leng = int(input())
    seq = input().replace('[', '').replace(']', '').split(',')
    if '' in seq:
        seq = []
    for order in Orders:
        if ((len(seq) == 0) and order=='D'):
            seq = 'error'
        elif order == 'R':
            seq.reverse()
        else:
            seq.pop(0)
    if seq != 'error':
        for j in range(len(seq)):
            seq[j] = int(seq[j])
    print(seq)
