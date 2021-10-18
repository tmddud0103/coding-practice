import sys
sys.stdin = open('input.txt')

def se(i, j):
    global mat, x, y
    q = [[i,j]]
    k = mat[i][j]
    mat[i][j] = 0
    while q:
        a, b = q.pop()
        for l in range(4):
            na = a+x[l]
            nb = b+y[l]
            if 0<=na<n and 0<=nb<n and mat[na][nb]==k:
                q.append([na, nb])
                mat[na][nb] = 0

def sese(i, j):
    global mat2, x, y
    q = [[i,j]]
    k = mat2[i][j]
    mat2[i][j] = 0
    while q:
        a, b = q.pop()
        for l in range(4):
            na = a+x[l]
            nb = b+y[l]
            if 0<=na<n and 0<=nb<n and mat2[na][nb]==k:
                q.append([na, nb])
                mat2[na][nb] = 0

def se2(i, j):
    global mat2, x, y
    q = [[i, j]]
    mat2[i][j] = 0
    while q:
        a, b = q.pop()
        for l in range(4):
            na = a + x[l]
            nb = b + y[l]
            if 0 <= na < n and 0 <= nb < n:
                if mat2[na][nb] == 'G' or mat2[na][nb] ==  'R':
                    q.append([na, nb])
                    mat2[na][nb] = 0

n = int(sys.stdin.readline().lstrip())
mat = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
mat2 = [item[:] for item in mat]

x = [1, -1, 0, 0]
y = [0, 0, 1, -1]
cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if mat[i][j]!=0:
            se(i, j)
            cnt1 += 1
        if mat2[i][j]!=0:
            if mat2[i][j] == 'B':
                sese(i, j)
                cnt2+=1
            else:
                se2(i, j)
                cnt2+=1
print('{} {}'.format(cnt1, cnt2))