import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline().rstrip()))
count = 0
for i in range(-1, -N-1, -1):
    if M == 0:
        break
    while coin[i] <= M:
        if coin[i]*1000 <= M:
            M -= coin[i]*1000
            count += 1000
        else:
            M -= coin[i]
            count += 1
print(count)