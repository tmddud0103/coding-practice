import sys

N = int(sys.stdin.readline().rstrip())
n = [0]*(N+5)
n[1] = 1
n[2] = 3
n[3] = 5
for i in range(4, N+1):
    n[i] = n[i-1] + n[i-2]*2
print(n[N]%10007)

