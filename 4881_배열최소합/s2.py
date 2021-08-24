import sys
sys.stdin = open('input.txt')

def recur(state):
    global total, min_number

    if sum(total) > min_number:
        return

    if state == N:
        tot = sum(total)
        if tot < min_number:
            min_number = tot

    else:
        for i in range(N):
            if i not in cannot_check:
                cannot_check.append(i)
                total.append(matrix[state][i])
                state += 1
                recur(state)
                state -= 1
                total.pop()
                cannot_check.pop()

test_case = int(input())
for tc in range(1, test_case + 1):
    N = int(input())
    matrix = []
    cannot_check = []
    total = []
    min_number = 10000
    for i in range(N):
        temp = list(map(int, input().split()))
        matrix.append(temp)
    recur(0)
    print('#{} {}'.format(tc, min_number))