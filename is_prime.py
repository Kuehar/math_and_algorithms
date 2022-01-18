"""
P.142
簡単な素数判定


def is_prime(N):
    for i in range(2,N):
        if N % i == 0:
            return False
    return True

N = int(input())
if is_prime(N):
    print("prime")
else:
    print("Not prime")

"""

"""
2以上の整数Nに対して
√Nまで調べて割り切れない場合は素数と判定するプログラム
P.143
"""

def is_prime(N):
    LIMIT = int(N**0.5)
    for i in range(2,LIMIT+1):
        if N % i == 0:
            return False
    return True

N = int(input())
if is_prime(N):
    print("prime")
else:
    print("Not prime")
