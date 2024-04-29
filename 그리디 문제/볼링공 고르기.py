import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = list(itertools.combinations(arr, 2))

cnt = 0
for i in result:
    if i[0] != i[1]:
        cnt += 1

print(cnt)