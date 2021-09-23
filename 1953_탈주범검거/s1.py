import sys
sys.stdin = open('input.txt')
TC = int(input())
for tc in range(1, TC+1):
    N, M, R, C, L = list(map(int, input().split()))
    matrix = []
    check_matrix = [[0 for _ in range(M)] for _ in range(N)]
    total = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        matrix.append(temp)
    queue = [[R, C]]
    #   하  상  우  좌
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]
    for i in range(1, L + 1):
        ran = len(queue)
        for i in range(ran):
            a = queue.pop(0)
            check_matrix[a[0]][a[1]] = 1
            total += 1
            #하
            if a[0]<N-1 and (matrix[a[0]][a[1]] == 1 or matrix[a[0]][a[1]] == 2 or matrix[a[0]][a[1]] == 5 or matrix[a[0]][a[1]] == 6) and (matrix[a[0]+x[0]][a[1]] == 1 or matrix[a[0]+x[0]][a[1]] == 2 or matrix[a[0]+x[0]][a[1]] == 4 or matrix[a[0]+x[0]][a[1]] == 7) and check_matrix[a[0]+x[0]][a[1]] == 0:
                queue.append([a[0]+x[0], a[1]])
            # 상
            if a[0] > 0 and (matrix[a[0]][a[1]] == 1 or matrix[a[0]][a[1]] == 2 or matrix[a[0]][a[1]] == 4 or matrix[a[0]][a[1]] == 7) and (matrix[a[0]+x[1]][a[1]] == 1 or matrix[a[0]+x[1]][a[1]] == 2 or matrix[a[0]+x[1]][a[1]] == 5 or matrix[a[0]+x[1]][a[1]] == 6) and check_matrix[a[0]+x[1]][a[1]] == 0:
                queue.append([a[0]+x[1], a[1]])
            # 우
            if a[1]<M-1 and (matrix[a[0]][a[1]] == 1 or matrix[a[0]][a[1]] ==  3 or matrix[a[0]][a[1]] ==  4 or matrix[a[0]][a[1]] ==  5) and (matrix[a[0]][a[1]+y[2]] == 1 or matrix[a[0]][a[1]+y[2]] == 3 or matrix[a[0]][a[1]+y[2]] == 6 or matrix[a[0]][a[1]+y[2]] == 7) and check_matrix[a[0]][a[1]+y[2]] == 0:
                queue.append([a[0], a[1] +y[2]])
            # 좌
            if a[1] > 0 and (matrix[a[0]][a[1]] == 1 or matrix[a[0]][a[1]] == 3 or matrix[a[0]][a[1]] == 6 or matrix[a[0]][a[1]] == 7) and (matrix[a[0]][a[1] + y[3]] == 1 or matrix[a[0]][a[1] + y[3]] == 3 or matrix[a[0]][a[1] + y[3]] == 4 or matrix[a[0]][a[1] + y[3]] == 5) and check_matrix[a[0]][a[1] + y[3]] == 0:
                queue.append([a[0], a[1] + y[3]])
    total2 = 0
    for i in range(N):
        for j in range(M):
            if check_matrix[i][j] == 1:
                total2 += 1
    print('#{} {}'.format(tc, total2))
