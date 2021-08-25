import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    TC = int(input())
    integer = list(map(int, input().split()))
    i = 1

    while integer[-1] != 0:
        a = integer.pop(0)
        if a - i <= 0:
            integer.append(0)
        else:
            integer.append(a-i)
        if i % 5 == 0 :
            i = 0
        i += 1
    print('#{}'.format(TC), end=' ')
    for i in integer:
        print(i, end=' ')
    print()
