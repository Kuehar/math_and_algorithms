# P.41
# 標準入力で数値、リストを受け入れる為の　list(map(int, input().split()))　を覚えよう
input_num = int(input())
a = list(map(int,input().split()))
ans = 0

for n in a:
    ans += n
print(ans)

"""
N = int(input())
A = list(map(int,input().split()))
Answer = 0
for item in A:
    Answer += item

print(Answer)
"""