ans = 0
# 下の二つの書き方は
# N = int(input())
# S = int(input())
# こういう風に書くと楽
N,S = map(int,input().split())

for i in range(1,N+1):
    for j in range(1,N+1):
        if i+j <= S:
            ans += 1


print(ans)