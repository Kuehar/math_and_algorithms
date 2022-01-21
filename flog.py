N = int(input())
H = list(map(int,input().split()))

dp = [None]*N
dp[0] = 0
for i in range(1,N):
    if i == 1:
        dp = abs(H[i-1]-H[i])
    if i >= 2:
        dp[i] = min(dp[i-1]+abs(H[i-2]-H[i]),dp[i-2]+abs(H[i-2]+H[i]))

print(dp[N-1])