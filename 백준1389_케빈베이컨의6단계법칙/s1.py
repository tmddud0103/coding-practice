import sys
sys.stdin = open('input.txt')

def keven_baken(i):
    global check, minbaken, mink
    q = [i]
    temp = 0
    while q:
        a = q.pop(0)
        for j in range(1, n+1):
            if mat[a][j] == 1 and check[j] == 0:
                q.append(j)
                check[j] = check[a] + 1
                temp += check[j]
                if temp > minbaken:
                    return
    if temp < minbaken:
        minbaken = temp
        mink = i

n, m = list(map(int, sys.stdin.readline().split()))
mat = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = list(map(int, sys.stdin.readline().split()))
    mat[x][y], mat[y][x] = 1, 1

minbaken = 6*1000
mink = 0
for i in range(1, n+1):
    check = [0]*(n+1)
    check[i] = 1
    keven_baken(i)
print(mink)