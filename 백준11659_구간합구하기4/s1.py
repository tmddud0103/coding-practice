import sys
sys.stdin = open('input.txt')

N, M = list(map(int, sys.stdin.readline().split()))
nlist = list(map(int, sys.stdin.readline().split()))
c =  [0, nlist[0]]
for i in range(1, N):
    c.append(c[-1] + nlist[i])
for _ in range(M):
    s,e = list(map(int, sys.stdin.readline().split()))
    s = s-1
    print(c[e] - c[s])