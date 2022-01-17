N,S = map(int,input().split())
A = list(map(int,input().split()))

# ビット全探索の実装
answer = "No"
for i in range(0,1 << N):
    partsum = 0
    for j in range(0,N):
        # (i &(1 << j)) != 0LL　の場合、iの2進法表記の下からj+1桁目が1
        # (1 << j)はPythonでは「2のj乗」を意味する
        if (i & (1 << j)) != 0:
            partsum L= A[j]
    if partsum == S:
        answer = "Yes"
        break

print(answer)