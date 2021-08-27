import sys
sys.stdin = open('s_input.txt')

T = int(input())

def check_danjo(num):
    num1 = num
    while num:
        temp1 = num % 10
        num = num // 10
        if num % 10 > temp1:
            return -1
    return num1

for tc in range(1, T + 1):
    N = int(input())
    a_list = list(map(int, input().split()))
    danjo = -1
    for i in range(0, N-1):
        for j in range(i+1, N):
            temp = a_list[i] * a_list[j]
            temp = check_danjo(temp)
            if temp > danjo:
                danjo = temp

    print('#{} {}'.format(tc, danjo))