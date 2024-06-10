def first(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
        return mid
    elif arr[mid] >= target:
        # 여기에 return을 쓰지 않으면 None이 반환된다.
        # 다음 재귀에서 return이 있더라도 여기에서 return 값이 없기 때문에 최종적으로 None을 반환하는듯..?
        return first(arr, start, mid - 1, target)
    else:
        return first(arr, mid + 1, end, target)

def last(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == len(arr)-1 or target < arr[mid + 1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return last(arr, start, mid - 1, target)
    else:
        return last(arr, mid + 1, end, target)

n, x = map(int, input().split())
arr = list(map(int, input().split()))

f = first(arr, 0, n-1, x)
l = last(arr, 0, n-1, x)

if f == None:
    result = -1
else:
    result = l - f + 1
print(result)