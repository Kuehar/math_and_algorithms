# P.204
N = int(input())
A = list(map(int,input().split()))

A.sort()


for i in range(N):
    print(A[i])