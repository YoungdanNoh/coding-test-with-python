s = input()
arr = list(map(int, s))

result = arr[0]
for i in range(1, len(arr)):
    if result <= 1 or arr[i] <= 1:
        result = result + arr[i]
    else:
        result = result * arr[i]
print(result)