import sys
sys.stdin = open('input.txt')

def q_go(q, mat):
    global n
    while q:
        a = q.pop()
        for i in range(n+1):
            if mat[a][i] == 1 and ch[i] == 0:
                ch[i] = 1
                q.append(i)

n, m = list(map(int, sys.stdin.readline().split()))
mat = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    mat[a][b], mat[b][a] = 1, 1
ch = [0]*(n+1)
cnt = 0
q = []
for i in range(1, n+1):
    if ch[i] == 0:
        cnt += 1
        ch[i] = 1
        q.append(i)
        q_go(q, mat)
print(cnt)