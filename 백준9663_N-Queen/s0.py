import sys

def queen_attack(i, j, board):
    global N
    bn = [item[:] for item in board]
    for k in range(N):
        bn[i][k] += 1
        bn[k][j] += 1
        if k + i < N and k + j < N:
            bn[i + k][j + k] += 1
        if i - k > -1 and j - k > -1:
            bn[i - k][j - k] += 1
        if i + k < N and j - k > -1:
            bn[i + k][j - k] += 1
    return bn

def queen(i, board):
    global cnt, N
    if i == N:
        cnt += 1
        return
    if 0 not in board[i]:
        return
    for j in range(N):
        if board[i][j] == 0:
            queen(i+1, queen_attack(i, j, board))

N = int(sys.stdin.readline().rstrip())
board = [[0]* N for _ in range(N)]
cnt = 0
queen(0, board)
print(cnt)