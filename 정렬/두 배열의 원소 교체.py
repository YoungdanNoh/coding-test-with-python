n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(k):
    if min(A) < max(B):
        A[A.index(min(A))], B[B.index(max(B))] = B[B.index(max(B))], A[A.index(min(A))]
    else:
        break

print(sum(A))