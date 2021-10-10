import sys
sys.stdin = open('input.txt')

n, m = list(map(int, sys.stdin.readline().split()))
betta = m - n +1

pm = int((m)**(1/2))
a = [False, False] + [True]*(pm)
primes = []
for i in range(2, pm+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, pm+1, i):
            a[j] = False
aaa = set()
for prime in primes:
    k = prime ** 2
    j = n//k
    # j = 1
    while k*j<n:
        j += 1
    while k*j <= m:
        aaa.add(k*j)

        j+=1

print(betta-len(aaa))

