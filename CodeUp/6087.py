n = int(input())

for i in range(n+1):
    if i%3 == 0:
        continue
    else:
        print(i, end=" ")