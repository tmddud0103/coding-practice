import sys
sys.stdin = open('input.txt')

test_case = int(input())

#0~9까지의 값 저장
count_number = [0]*10



n = int(input())
for i in range(n):
    lst = list(map(int, input()))
    cnt_lst = [0] * 10
    for i in lst:
        cnt_lst[i] += 1

    print(cnt_lst)