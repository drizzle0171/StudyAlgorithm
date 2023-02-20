# import sys
# input = sys.stdin.readline

# n = int(input())
# words = []
# chars = set()
# for _ in range(n):
#     word = input().rstrip()
#     words.append(word)
#     for i in word:
#         chars.add(i)

# chars = sorted(list(chars))
# dictionary = {}
# j = 9

# for i in range(len(chars)):
#     dictionary[chars[i]] = str(j)
#     j -= 1

# result = []
# for word in words:
#     temp = ''
#     for i in word:
#         temp += dictionary[i]
#     result.append(temp)

# total = 0
# for word in result:
#     total += int(word)
# print(total)

import sys

n = int(sys.stdin.readline())

alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alphabet_list = []
answer = 0
pocket = []

for _ in range(n):
    alphabet = input()
    pocket.append(alphabet)

for alphabet in pocket:
    for i in range(len(alphabet)):
        num = 10 ** (len(alphabet) - i - 1)
        alphabet_dict[alphabet[i]] += num

for value in alphabet_dict.values():
    if value > 0:
        alphabet_list.append(value)

sorted_list = sorted(alphabet_list, reverse=True)
for i in range(len(sorted_list)):
    answer += sorted_list[i] * (9 - i)

print(answer)