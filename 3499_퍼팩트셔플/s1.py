import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    cards = list(map(str, input().split(' ')))
    first_cards = cards[:(N+1)//2]
    last_cards = cards[(N+1)//2:]
    shuffle = []
    while len(shuffle) != N:
        shuffle.append(first_cards.pop(0))
        if len(last_cards) > 0:
            shuffle.append(last_cards.pop(0))
    print('#{} '.format(tc), end ='')
    for i in range(N):
        print(shuffle[i], end = ' ')
    print()