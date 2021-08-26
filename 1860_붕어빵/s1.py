import sys
sys.stdin = open('input.txt')

TC = int(input())

def fishbread():
    global lists
    for i in range(N):
        lists[i] = lists[i] // M
        if lists[i] == 0:
            return 'Impossible'
    lists.sort()
    bread = 0
    for i in range(1, lists[-1]+1):
        bread += K
        count = 0
        if i == lists[0]:
            a = lists.pop(0)
            count += 1
            while not len(lists) == 0 and lists[0] == a:
                count += 1
                lists.pop(0)
        bread -= count
        if bread < 0:
            return 'Impossible'
    return 'Possible'

for tc in range(1, 142):
    # N명의 사람
    # M초의 시간, K개의 붕어빵
    N, M, K = list(map(int, input().split()))
    lists = list(map(int, input().split()))
    print('#{} {}'.format(tc, fishbread()))
