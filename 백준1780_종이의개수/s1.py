import sys
sys.stdin = open('input.txt')


def chch(l, x, y):
    global mat, ch0_11
    temp = mat[x][y]
    if l == 1:
        ch0_11[mat[x][y]] += 1
        return
    for i in range(x, x+l):
        for j in range(y, y+l):
            if temp != mat[i][j]:
                k = [0, l//3, (2*l)//3]
                for ck in range(3):
                    for ck2 in range(3):
                        chch(l//3, x + k[ck], y + k[ck2])
                return
    ch0_11[mat[x][y]] += 1
    return



n = int(sys.stdin.readline().lstrip())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ch0_11 = {-1 : 0, 0 : 0, 1 : 0}
chch(n, 0, 0)
print(ch0_11[-1])
print(ch0_11[0])
print(ch0_11[1])