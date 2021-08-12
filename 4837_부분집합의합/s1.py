import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case + 1):
    N, K = list(map(int, input().split()))
    can_be_subset = 0
    list12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in range(1 << 12):
        sum_of_subset = 0
        subset = []
        for j in range(13):
            if i & (1 << j):
                subset += [list12[j]]
        for i in range(0, len(subset)):
            sum_of_subset += subset[i]

        if sum_of_subset == K and len(subset) == N:
            can_be_subset += 1
    print('#{} {}'.format(tc, can_be_subset))