import sys

binary = list(map(int, sys.stdin.readline().strip()))
if len(binary) % 3 != 0:
    while len(binary) % 3 !=0:
        binary.insert(0, 0)

binary_list = []
temp = []
for i in range(0, len(binary), 3):
    for j in binary[i:i+3]:
        temp.append(j)
    binary_list.append(temp)
    temp = []
        
octal = ''

for i in range(len(binary_list)):
    octal += str(binary_list[i][0]*4 + binary_list[i][1]*2 + binary_list[i][2]*1)
        
print(int(octal))