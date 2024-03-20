import sys

n = int(sys.stdin.readline().rstrip())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
m_arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(m):
    for j in range(len(n_arr)):
        if m_arr[i] == n_arr[j]:
            print('yes', end=' ')
            break
        elif j == (len(n_arr)-1):
            print('no', end=' ')