import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs():
    temp_case = []
    case = []
    global max_number
    if max_number >= 2:
        temp_case.append(2)
        while max_number >= sum(temp_case) + 2:
            temp_case.append(2)
        if max_number > sum(temp_case):
            temp_case.append(1)
    case.append(temp_case[:])
    while len(temp_case):
        if len(temp_case) > 0:
            if temp_case[-1] == 2:
                temp_case.pop()
                temp_case.append(1)
                while max_number >= sum(temp_case) + 2:
                    temp_case.append(2)
                while max_number == sum(temp_case) + 1:
                    temp_case.append(1)
                case.append(temp_case[:])
            else:
                temp_case.pop()
        else:
            pass
    return case

for tc in range(1, T + 1):
    N = int(input())
    max_number = N // 10
    count = 0
    number_list = []
    matrix = dfs()
    for i in range(0, len(matrix)):
        multi_count = 0
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                multi_count += 1
        count += 1 * (2 ** multi_count)
    print(f'#{tc} {count}')


