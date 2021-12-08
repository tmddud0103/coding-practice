import sys
sys.stdin = open('sample_input.txt')

test_case = int(input())

for tc in range(1, test_case + 1):
    n, m = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                for k in range(i, n):
                    mat[k][j] = 0
    deep = 1
    position = -1
    total = 0
    eat = [1]

    while eat:
        eat.pop()
        # print(deep, position)
        if deep > n:
            deep = n
        for i in range(m+1):
            pr = position + i
            pl = position - i

            for j in range(deep):
                if 0<=pr<m and mat[j][pr] == 1:
                    mat[j][pr] = 0
                    eat.append(1)
                    total += abs(pr-position)+1
                    deep += 1
                    position = pr
                    break
                if 0<=pl<m and mat[j][pl] == 1:
                    mat[j][pl] = 0
                    eat.append(1)
                    total += abs(pl - position)+1
                    deep += 1
                    position = pl
                    break
            if len(eat) != 0:
                print(mat)
                break
    print('#{} {}'.format(tc,total))