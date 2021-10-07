import sys
def queen(now):
    global cnt, N, check
    if now == N+1:
        cnt += 1
        # print(check)
        return
    for i in range(N):
        if check[i] == 'o':
            if now == 1:
                check[i] = now
                queen(now + 1)
                check[i] = 'o'
            else:
                if i>0 and check[i-1]==now-1:
                    pass
                elif i<N-1 and check[i+1]==now-1:
                    pass
                else:
                    check[i] = now
                    queen(now+1)
                    check[i] = 'o'


N = int(sys.stdin.readline().rstrip())
board = [[0]* N for _ in range(N)]
cnt = 0
check = ['o']*N
queen(1)
print(cnt)