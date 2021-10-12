import sys
sys.stdin = open('input.txt')

def dong(i, j):
    global n, mat, total, cnt, x1, y1
    temp = 1
    mat[i][j] = 0
    q = [[i, j]]
    while q:
        x, y = q.pop()
        for k in range(4):
            nx = x+x1[k]
            ny = y+y1[k]
            if 0<=nx<n and 0<=ny<n and mat[nx][ny] == 1:
                q.append([nx, ny])
                mat[nx][ny] = 0
                temp += 1
    return temp

n = int(sys.stdin.readline().lstrip())
mat = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
total = 0
cnt = []
x1 = [1, -1, 0, 0]
y1 = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            a = dong(i, j)
            cnt.append(a)
            total += 1
print(total)
cnt.sort()
for i in range(total):
    print(cnt[i])