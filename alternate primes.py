from math import isqrt
N = int(input("Enter the limit: "))
primes = []
for i in range (2, N+1):
    is_prime = True
    for j in range(2, isqrt(i)+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print(primes[::2])