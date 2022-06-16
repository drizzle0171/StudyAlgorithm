import sys
import numpy as np

binary = list(map(int, sys.stdin.readline().strip()))
if len(binary) % 3 != 0:
    while len(binary) % 3 !=0:
        binary.insert(0, 0)

binary = np.array(binary).reshape(-1, 3)
octal = ''

for i in range(len(binary)):
    octal += str(binary[i][0]*4 + binary[i][1]*2 + binary[i][2]*1)
        
print(int(octal))