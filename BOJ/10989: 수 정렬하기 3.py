# 병합정렬 사용하기!

def merge_sort(array):

    # 분할하기
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j<len(right):
            array[k] = right[j]
            j+=1
            k+=1
    elif j == len(right):
        while i<len(left):
            array[k] = left[i]
            i+=1
            k+=1
    return array

N = int(input())
array = [int(input()) for i in range(N)]

ordered_array = merge_sort(array)

for i in range(N):
    print(array[i])

# RecursionError는 재귀와 관련된 에러입니다. 가장 많이 발생하는 이유는 Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때입니다.

