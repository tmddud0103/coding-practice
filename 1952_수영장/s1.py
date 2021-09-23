import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    D, M, M3, Y = list(map(int, input().split()))
    year = list(map(int, input().split()))
    sum_year = [0 for _ in range(13)]
    for i in range(len(year)):
        year[i] = year[i] * D
        if year[i] > M:
            year[i] = M
    for i in range(1, len(year)+1):
        if i > 1:
            sum_year[i] = sum_year[i-1] + year[i-1]
        else:
            sum_year[1] = year[0]
        if i > 2:
            sum_year[i] = min(sum_year[i-3] + M3, sum_year[i])

    print("#{} {}".format(tc,min(sum_year[-1], Y)))
