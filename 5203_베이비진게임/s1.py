import sys
sys.stdin = open('sample_input.txt')

def ch_babygin(c_list):
    for i in range(len(c_list)-2):
        if c_list[i] == c_list[i+1] == c_list[i+2]:
            return 1
        if c_list[i]+1 in c_list and c_list[i]+2 in c_list:
            return 1
    return 0



TC = int(input())

for tc in range(1, TC+1):
    cardlist = list(map(int, input().split()))
    a = []
    b = []
    for i in range(6):
        a.append(cardlist[2 * i])
        b.append(cardlist[2 * i + 1])
        if i >= 2:
            p1 = ch_babygin(sorted(a))
            p2 = ch_babygin(sorted(b))
            if p1 == 1 or p2 == 1:
                break
    if p1 > p2:
        print('#{} {}'.format(tc, 1))
    elif p1 < p2:
        print('#{} {}'.format(tc, 2))
    elif p1 == 1 and p1 == p2:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))