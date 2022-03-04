# 입력이 주어졌을 때 오름차순으로 정렬하는 프로그램

Num = int(input()) # 수의 개수

num_list = [int(input()) for _ in range(Num)] # 숫자 입력

# ordered_list = num_list.sort()
# object.sort()는 객체 자체를 변환
# sorted(object)는 새로운 객체를 반환

for i in range(Num):
    print(num_list[i])