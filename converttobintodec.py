# P.48
N = int(input())
answer = ""

while N >= 1:
    # N%2 -> Nを2で割ったあまり
    # N//2 はNを2で割った値の整数部分
    if N%2 == 0:
        answer = "0"+answer
    if N%2 == 1:
        answer = "1"+answer
    N = N //2
print(answer)