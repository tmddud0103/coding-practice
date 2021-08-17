import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case + 1):
    lazer = input()
    lazer_beam = lazer.replace( '()', 'B')
    print(lazer_beam)
    # n = 전체 막대기의 개수
    # total = 전체 토막의 개수
    n = 0
    total = 0
    for i in lazer_beam:
        if i == '(':
            n += 1
            total += 1
        elif i == 'B':
            total += n
        else:
            n -= 1
    print('#{} {}'.format(tc, total))