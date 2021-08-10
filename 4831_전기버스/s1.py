import sys
sys.stdin = open('input.txt')

test_case = int(input())
# K = 한번 충전에 최대 갈 수 있는거리
# N = 마지막 정류장 번호
# M = 충전기가 설치된 정류장 갯수
# location_of_electric_station = 충전기가 설치된 정류장 번호
for test in range(1, test_case + 1):
    K, N, M = list(map(int, input().split()))
    location_of_electric_station = list(map(int, input().split()))
    number_of_refill_electric = 0
    #현재 버스가 움직일 수 있는 거리
    bus_can_move = K
    for bus in range(1, N + 1):
        bus_can_move -= 1
        # 버스가 갈수있는거리가 -1이다 = 충전기 설치가 잘못되어서 종점에 못간다
        # 브레이크 걸고 충전 횟수를 0으로 바꾼다
        if bus_can_move == -1:
            number_of_refill_electric = 0
            break
        #현재 위치가 충전소(마지막 충전소를 제외)일 경우
        for i in range(0, M - 1):
            if bus == location_of_electric_station[i]:
                #다음 충전소까지 갈 수 있을때
                if bus + bus_can_move >= location_of_electric_station[i+1]:
                    continue
                #다음 충전소까지 못가고 충전을 해야 할 때
                else:
                    number_of_refill_electric += 1
                    bus_can_move = K
        #현재 위치가 마지막 충전소인 경우
        if bus == location_of_electric_station[M-1]:
            # 충천 안하고끝까지 갈 때
            if bus + bus_can_move >= N:
                continue
            # 충전을 해야 끝까지 갈 때
            else:
                number_of_refill_electric += 1
                bus_can_move = K
    print('#{} {}'.format(test, number_of_refill_electric))
