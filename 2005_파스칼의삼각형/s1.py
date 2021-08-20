import sys
sys.stdin = open('input.txt')

T = int(input())

def pascal(n):
    p1 = [1]
    p2 = [1, 1]
    p_odd = [0] * n
    p_even = [0] * n
    if n == 1:
        print(p1[0])
    elif n == 2:
        print(p1[0])
        print(p2[0], p2[1])
    else:
        print(p1[0])
        print(p2[0], p2[1])
        cycle = 3
        p_even[0] = p_even[1] = 1
        while cycle <= n:
            if cycle % 2:
                p_odd[0] = 1
                for i in range(1, cycle):
                    p_odd[i] = p_even[i - 1] + p_even[i]
                p_odd[cycle - 1] = 1
                cycle += 1
                for i in p_odd:
                    if i != 0:
                        print(i, end=' ')
                print()
            else:
                p_even[0] = 1
                for i in range(1, cycle - 1):
                    p_even[i] = p_odd[i - 1] + p_odd[i]
                p_even[cycle - 1] = 1
                cycle += 1
                for i in p_even:
                    if i != 0:
                        print(i, end=' ')
                print()
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    pascal(N)