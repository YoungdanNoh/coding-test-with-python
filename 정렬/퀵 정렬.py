arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개라면 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            # 피벗보다 큰 데이터를 찾는다
            # left <= end는 [1,0]과 같은 배열을 정렬할 때 무한반복문이 되지 않고
            # 정상적으로 정렬하기 위해 left = 2로 만들어 줄 수 있도록 하기 위함이다.
            left += 1
        while right > start and array[right] >= array[pivot]:
            # 피벗보다 작은 데이터를 찾는다
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(arr, 0, len(arr) - 1)
print(arr)
