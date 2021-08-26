import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = list(map(int, input().split()))
    # N = 화덕의 크기 = N개의 피자를 동시에 굽는다
    # M = 피자 개수
    pizza = list(map(int, input().split()))
    circle = []
    wha_duck = []
    # 1부터 M까지 숫자를 circle에 집어넣는다
    for i in range(1, M + 1):
        circle.append(i)
    # 화덕에 circle에 넣을 수 있는 갯수만큼 = N개만큼 넣는다
    # 화덕에서는 숫자만(피자의 순서를 나타내는 숫자) 돌리고 피자는 따로 계산을 할 생각
    for i in range(N):
        a = circle.pop(0)
        wha_duck.append(a)
    count = 0
    # 화덕에 아무것도 없을 때까지
    while len(wha_duck) != 0:
        a = wha_duck.pop(0)
        # 피자 안에 있는 치즈가 다 녹았을 때
        if pizza[a-1] == 0:
            if len(circle) != 0:
                a = circle.pop(0)
                # 만약 이번 서클에있는 넘버가 마지막이라면 = 마지막 피자
                # while문이 끝나고 a의 값에는 마지막 피자의 숫자가 저장되게 된다
                wha_duck.insert(0, a)
        # 안녹았을 때
        else:
            wha_duck.append(a)
        # 카운트를 센다
        count += 1
        # 한바퀴를 다 돌았으면 피자(치즈)를 반띵
        if count % N == 0:
            for i in range(len(wha_duck)):
                pizza[wha_duck[i]-1] = pizza[wha_duck[i]-1] // 2
    print('#{} {}'.format(tc, a))
