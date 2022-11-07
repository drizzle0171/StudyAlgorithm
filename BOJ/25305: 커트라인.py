N, k = map(int, input().split())
people = sorted(list(map(int, input().split())), reverse=True)
print(people[k-1])

