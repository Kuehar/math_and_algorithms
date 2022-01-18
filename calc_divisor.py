# 約数を小さい順に出力するプログラム

N = int(input())

LIMIT = int(N**0.5)
divisors = []
for i in range(1,LIMIT+1):
    if N % i == 0:
		divisors.append(i)
		if i != N // i:
			divisors.append(N // i)

# 小さい順に並べ替え → 出力
# sort は小さい順に並べ替える関数です（3.6.1 項で扱います）
divisors.sort()
for i in divisors:
	print(i)