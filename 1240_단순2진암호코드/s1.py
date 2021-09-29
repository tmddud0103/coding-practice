import sys
sys.stdin = open('input.txt')

def searchNotZero():
    global matrix, N, M
    for i in range(N):
        for j in range(M-1, -1, -1):
            if matrix[i][j] == 1:
                return (i, j)

def searchPassword():
    global matrix, N, M, row_line
    cnt = []
    j = 0
    for _ in range(8):
        temp = matrix[row_line[0]][row_line[1]-6-j : row_line[1]+1-j]
        temp = checkPassword(temp)
        cnt.append(temp)
        j += 7
    return cnt

def checkPassword(pass_list):
    if pass_list == [0, 0, 0, 1, 1, 0, 1]:
        return 0
    elif pass_list == [0, 0, 1, 1, 0, 0, 1]:
        return 1
    elif pass_list == [0, 0, 1, 0, 0, 1, 1]:
        return 2
    elif pass_list == [0, 1, 1, 1, 1, 0, 1]:
        return 3
    elif pass_list == [0, 1, 0, 0, 0, 1, 1]:
        return 4
    elif pass_list == [0, 1, 1, 0, 0, 0, 1]:
        return 5
    elif pass_list == [0, 1, 0, 1, 1, 1, 1]:
        return 6
    elif pass_list == [0, 1, 1, 1, 0, 1, 1]:
        return 7
    elif pass_list == [0, 1, 1, 0, 1, 1, 1]:
        return 8
    elif pass_list == [0, 0, 0, 1, 0, 1, 1]:
        return 9
    else:
        return 'pass'



TC = int(input())

for tc in range(1, TC + 1):
    N, M = list(map(int, input().split()))
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input())))
    row_line = searchNotZero()
    answer = searchPassword()
    ans1 = 0
    ans = 0
    for i in range(0, len(answer)):
        if i == 0:
            ans += answer[i]
        elif i % 2 == 1:
            ans += answer[i]*3
        else:
            ans += answer[i]
        ans1 += answer[i]

    if ans % 10 != 0:
        ans1 = 0
    print(f'#{tc} {ans1}')


