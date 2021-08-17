import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case + 1):
    N = str(input())
    M = str(input())
    result = 0
    for i in range(0, len(M) - len(N) + 1):
        if N[0] == M[i]:
            check = 0
            for j in range(0, len(N)):
                if N[j] == M[i + j]:
                    check += 1
            if check == len(N):
                result = 1
    print('#{} {}'.format(tc, result))

