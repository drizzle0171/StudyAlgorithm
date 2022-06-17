import sys

decimal = int(sys.stdin.readline())
minus_bin = ''

while True:
    if decimal == 0:
        break
    if decimal == (1 or -1):
        break
    if decimal%2 !=0:
        decimal = (decimal-1)//-2
        minus_bin += '1'
    else:
        minus_bin += (str(decimal%-2))
        decimal = decimal//-2

if decimal == -1:
    minus_bin += '11'
else:
    minus_bin += str(decimal)

print(int(minus_bin[::-1]))