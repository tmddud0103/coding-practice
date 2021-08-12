import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case + 1):
    color_index = []
    for i in range(10):
        color_index +=[[0] * 10]
    N = int(input())
    for n in range(N):
        case = list(map(int, input().split()))
        for i in range(10):
            for j in range(10):
                if case[0] <= i <= case[2]:
                    if case[1] <= j <= case[3]:
                        if color_index[i][j] == 0:
                            color_index[i][j] = case[4]
                        elif color_index[i][j] == case[4]:
                            continue
                        else:
                            color_index[i][j] += case[4]
        total = 0
        for i in range(10):
            for j in range(10):
                if color_index[i][j] >= 3:
                    total += 1
    print('#{} {}'.format(tc, total))