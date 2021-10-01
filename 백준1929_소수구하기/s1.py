import sys
sys.stdin = open('input.txt')

def primes(p):
    global M, N
    for i in p:
        if i > N:
            return 0
        if i >= M:
            print(i)

M, N = list(map(int, input().split()))
scale = 1000000
a = [False, False] + [True]*(scale-1)
prime = []
for i in range(2, scale+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i, scale+1, i):
            a[j]=False
primes(prime)

