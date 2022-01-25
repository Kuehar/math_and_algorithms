# P.423
N,K = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)

if S % 2 != K % 2:
    print("No")
elif S > K:
    print("No")
else:
    print("Yes")