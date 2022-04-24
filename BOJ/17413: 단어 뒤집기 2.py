import sys

sentence = list(sys.stdin.readline().strip())
tag = False
word = ''
result = ''

for i in sentence:
    if tag == False:
        if i == '<':
            tag = True
            word += i
        elif i == ' ':
            word += i
            result += word
            word = ''
        else:
            word = i+word
    elif tag == True:
        word += i
        if i=='>':
            tag = False
            result += word
            word = ''

print(result + word)
