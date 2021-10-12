import sys
from itertools import product
sys.stdin = open('sample_input.txt')

def brickbreak(permu, maptemp):
    global n, w, h, total
    if total == w*h:
        return
    temp = 0
    for p in permu:
        for j in range(h):
            if maptemp[j][p] != 0:
                if maptemp[j][p] == 1:
                    temp += 1
                    maptemp[j][p] = 0
                    break
                else:
                    temp = killbrick(j, p, temp, maptemp)
                    maptemp = gravity(maptemp)
                    break
    if temp > total:
        total = temp

def killbrick(i, j, temp, maptemp):
    global n, w, h, x, y
    q = [[maptemp[i][j], i, j]]
    maptemp[i][j] = 0
    temp += 1
    while q:
        k, a, b = q.pop(0)
        for ni in range(4):
            for kk in range(1, k):
                nx = a +x[ni]*kk
                ny = b +y[ni]*kk
                if 0<=nx<h and 0<=ny<w and maptemp[nx][ny] != 0:
                    if maptemp[nx][ny] ==1:
                        maptemp[nx][ny] = 0
                        temp += 1
                    else:
                        q.append([maptemp[nx][ny], nx, ny])
                        maptemp[nx][ny] = 0
                        temp += 1
    return temp

def gravity(maptemp):
    global w, h
    for j in range(w):
        for i in range(h-1, -1, -1):
            if maptemp[i][j] == 0:
                for k in range(i, -1, -1):
                    if maptemp[k][j] != 0:
                        maptemp[i][j], maptemp[k][j] = maptemp[k][j], maptemp[i][j]
                        break
    return maptemp


TC = int(input())

for tc in range(1, TC + 1):
    n, w, h = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for _ in range(h)]
    temp1 = 0
    for i in range(h):
        for j in range(w):
            if mat[i][j]!= 0:
                temp1 +=1
    x = [1, -1, 0, 0]
    y = [0, 0, -1, 1]
    total = 0
    per = []
    if n == 1:
        for i in product(range(w)):
            per.append(i)
    elif n ==2:
        for i in product(range(w), range(w)):
            per.append(i)
    elif n == 3:
        for i in product(range(w), range(w), range(w)):
            per.append(i)
    else:
        for i in product(range(w), range(w), range(w), range(w)):
            per.append(i)
    for i in range(len(per)):
        maptemp = [item[:] for item in mat]
        brickbreak(per[i], maptemp)
    print("#{} {}".format(tc, temp1 - total))