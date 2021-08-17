import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case + 1):
    A, B = list(map(str, input().split()))
    count_num = A.count(B)
    print('#{} {}'.format(tc, len(A) - (count_num * len(B)) + count_num))