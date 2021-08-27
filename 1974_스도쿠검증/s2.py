import sys
sys.stdin = open('input.txt')

def sudoku(mat):
    cnt1 = [0] * 10
    cnt2 = [0] * 10
    cnt3 = [0] * 10
    for i in range(9):
        cnt2 = [0] * 10
        cnt3 = [0] * 10
        for j in range(9):
            if i%3 == 0 and j%3 == 0:
                cnt1 = [0] * 10
                for l in range(0, 3):
                    for m in range(0, 3):
                        cnt1[mat[i+l][j+m]] += 1
                        if cnt1[mat[i][j]] != 1:
                            return 0
            cnt2[mat[i][j]] += 1
            cnt3[mat[j][i]] += 1
            if cnt2[mat[i][j]] != 1 or cnt3[mat[j][i]] != 1:
                return 0
    return 1

TC = int(input())
for tc in range(1, TC + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, sudoku(matrix)))
