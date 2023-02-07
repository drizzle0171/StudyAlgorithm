document = input()
word = input()

len_docu = len(document)
len_word = len(word)
i = 0
count = 0

for _ in range(len_docu-len_word+1):
    if document[i:i+len_word] == word:
        count += 1
        i += len_word
    else:
        i += 1
        
print(count)