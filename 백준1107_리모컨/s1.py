import sys
sys.stdin = open('input.txt')
remo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

n = str(sys.stdin.readline().lstrip())
intn = int(n)
brokennumber = int(sys.stdin.readline().lstrip())
nn = list(map(int, sys.stdin.readline().split()))
for i in range(brokennumber):
    remo[nn[i]] = 0
memo = []
for i in range(len(n)):
    if remo[int(n[i])]==0:
        for j in range(1, 10):
            if remo[int(n[i])+j] == 1:
                n[i]