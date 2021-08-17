import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case + 1):
    N, M = list(map(int, input().split()))
    matrix = []
    result = ''
    for i in range(N):
        row_matrix = list(map(str, input()))
        matrix.append(row_matrix)
    for i in range(0, N):
        for j in range(0, N - M + 1):
            if matrix[i][j] == matrix[i][j + M - 1]:
                k = 0
                count = 0
                # k는 0부터
                # 예시 3번째부터 10개의 단어를 비교할때 3~12번째의 단어를 비교
                # 3, 12번째 비교
                # 4, 11번째 비교
                # . . .
                # 7, 8번째 비교
                # 각각의 비교시 알파벳이 같다면 count +1
                while j + k <= (j + M - 1 - k):
                    k += 1
                    if matrix[i][j + k] == matrix[i][j + M - 1 - k]:
                        count += 1
                # 회문일 경우 카운트는 항상 M/2보다 크거나 같다
                if count >= M / 2:
                    for alp in range(0, M):
                    # result
                        result += matrix[i][j + alp]
            if matrix[j][i] == matrix[j + M - 1][i]:
                k = 0
                count = 0
                while j + k <= (j + M - 1 - k):
                    k += 1
                    if matrix[j + k][i] == matrix[j + M - 1 - k][i]:
                        count += 1
                if count >= M / 2:
                    for alp in range(0, M):
                        # result
                        result += matrix[j + alp][i]
    print('#{} {}'.format(tc, result))
