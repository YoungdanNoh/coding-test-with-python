s = input()

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sum = 0
result =''
for i in s:
    if i in arr:
        sum += int(i)
    else:
        result += i

print(*sorted(result), sep='', end='')
print(sum)