a = list(map(int, input().split(" ")))

even = [i for i in a if i%2 == 0]
print(*even, sep="\n")