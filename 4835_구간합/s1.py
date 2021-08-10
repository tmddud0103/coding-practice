import sys
sys.stdin = open('input.txt')

test_case = int(input())
for test in range(1, test_case + 1):
    # N 전체 갯수
    # M 합치는 갯수
    N, M = list(map(int, input().split()))
    list_of_numbers = list(map(int, input().split()))
    # 최대 100개의 정수 N과 각각 최댓값 10000을 받을 수 있다
    # 그래서 최솟값에 100 * 10000 = 1000000인 코드상의 최댓값을 사용
    min_number = 1000000
    max_number = 0
    # M만큼을 합치게 되면
    # N개의 정수에서 이웃한 M개의 합을 계산하는 경우의 수는
    # N-M+1이다
    # 예시) 5개의 정수에서(1, 2, 3, 4, 5) 이웃한 3개의 합을 계산하는 경우
    # (1, 2, 3) ... (3, 4, 5) : 3가지 경우의 수 (N - M + 1) 수학적!
    for i in range(0, N - M + 1):
        # 구간별로 합친 숫자를 잠시 저장하는 용도
        # temp를 이용해 최댓값과 최솟값을 비교해서 저장할 계획
        temp = 0
        # i 번째 정수에서 시작해서 M개의 정수를 더하는 방법
        # (i) + (i + 1) + ... + (i + M - 1) 괄호의 갯수가 M개
        # 0th +  1th   + ...  +   (m-1)th
        # 위의 방식을 사용하기 위해 밑의 j를 0부터 M-1번째까지 반복
        # 반복한 j를 i에 더하여서 시작값과 끝값을 나타낸다
        for j in range(0, M):
            temp += list_of_numbers[i + j]
        if temp > max_number:
            max_number = temp
        if min_number > temp:
            min_number = temp
    print('#{} {}'.format(test, max_number - min_number))