import sys
sys.stdin = open('input.txt')


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    if N == 0:
        print('1 0')
    elif N == 1:
        print('0 1')
    else:
        memo = [0] * 41
        memo[0] = [1, 0]
        memo[1] = [0, 1]
        for i in range(2, 41):
            memo[i] = [memo[i-1][0]+memo[i-2][0], memo[i-1][1]+memo[i-2][1]]
        print(*memo[N], sep =' ')










        # box = []
        # cnt0 = 0
        # cnt1 = 0
        # box.append(N-1)
        # box.append(N-2)
        # while box:
        #     x = box.pop(0)
        #     if x == 0:
        #         cnt0 += 1
        #     elif x == 1:
        #         cnt1 += 1
        #     else:
        #         box.append(x - 1)
        #         box.append(x - 2)
        # print('{} {}'.format(cnt0, cnt1))