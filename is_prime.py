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