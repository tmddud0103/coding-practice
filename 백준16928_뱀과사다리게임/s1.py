import sys
sys.stdin = open('input.txt')

def gogo(now, howmany):
    global total
    k = 0
    if howmany > total:
        return
    for i in range(1, 7):
        if now + i == 100:
            if total > howmany:
                total = howmany+1
            return
        if game[now + i] == 0 and k < now + i:
            k = now + i
        else:
            temp, game[now+i] = game[now+i], 0
            gogo(temp, howmany+1)
            game[now + i] = temp
    gogo(k, howmany+1)


game = [0]*101
n, m = list(map(int, sys.stdin.readline().split()))
for _ in range(n+m):
    a, b = list(map(int, sys.stdin.readline().split()))
    game[a] = b
total = 100
gogo(1, 0)
print(total)

