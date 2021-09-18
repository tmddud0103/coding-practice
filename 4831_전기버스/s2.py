import sys
sys.stdin=open('input.txt')
case_num = int(input())         # test Case 받아오는것.
now_pos = 0                     #현재 위치 변수 설정
refill_gas = 0                  #충전 횟수 변수 설정

for m in range(case_num):       #각 test Case 별 구문
    size_move, size_stop, size_charge = list(map(int, input().split()))
     #Size Move = 충전 한번에 움직일 수 있는 정류장 수
     #Size _Stop = 노선의 총 정류장 수
     # Size Charge = 노선 내 충전소 갯수

    fuel_tank = int(size_move) #Fuel tank는 버스의 남은 연료 표기
    pos_charge = list(map(int, input().split()))
    #Pos_charge는 정류장의 위치
    charge_stop = [False]*(size_stop+1)
    c_p = 0
    # Null list 를 만들줄 몰라서, 억지로 1by 10짜리 Array를 만든거임.
    # print(f'size_move : {size_move}') #표기용
    # print(f'size_stop : {size_stop}') #표기용
    # print(f'size_charge : {size_charge}') #표기용
    # print(f'pos_charge : {pos_charge}') #표기용

    for j in pos_charge:
        charge_stop[j] = True # 충전소 위치를 True로 표기하기로함.
    # print(charge_stop)
    for k in range(size_stop):
        now_pos = now_pos + 1
        fuel_tank = fuel_tank - 1
        if fuel_tank < 0:
            c_p = 1
            # print(f'run out of gases')
            break

        else:
            # print(f'now we are in {now_pos}')
            # print(f'now we have {fuel_tank} more gases')
            determinant = []

            if k+1 < size_stop and charge_stop[k+1] == True:
                #1. 1칸 이동시마다,
                #2. 현 이동 위치가, 정류소 갯수 이하만큼 왔는지 확인 (조건1)
                #3. 해당 위치가 충전소인지 위치 확인 (조건2)
                for temp_search in range(fuel_tank):
                    #남은 연료만큼 더 가면 충전이 가능한지 체크위함
                    # 남은 연료 2 일시, 0~1 출력
                    if charge_stop[k+1+temp_search+1] == True:
                        #k+1 : 현재 이동위치
                        #temp_search+1 : 남은 연료 표시.
                        # 조건문 : 현재 위치 기준으로 최대 이동 가능 거리 內 충전소 있는지 확인
                        determinant.append(1) #충전소 있을시 Det = 1
                    else:
                        determinant.append(0) #충전소 없을시 Det = 0

                # print(f'it is determinant {determinant}')
                # print(f'it is sum of determinant {sum(determinant)}')

                if sum(determinant)>0:
                    #충전소 있을시 Det =1 이므로, 충전하지 않고 이동
                    refill_gas = refill_gas
                    fuel_tank = fuel_tank
                    determinant = []
                    # print(refill_gas)
                else:
                    # 충전소 없을시, 충전이 필요하나, 맨끝이 다가왔을때는 그냥 가도록 설정
                    if fuel_tank >= ((size_stop)-now_pos):
                    #현재 위치가 끝 충전소이고, 남은 연료로 충분히 갈 수 있다고 하면 충전 안함
                        refill_gas = refill_gas
                        fuel_tank = fuel_tank
                        determinant = []
                    else:
                    # 현재 위치가 끝 충전소가 아니고, 남은 연료로 충분히 갈 수 없으면 충전
                        refill_gas = refill_gas+1
                        # print(f'Refilled gas')
                        fuel_tank = size_move
                        determinant = []

            else:
                refill_gas = refill_gas
                fuel_tank = fuel_tank
                determinant = []
                # print(refill_gas)

    mod_check = size_stop//size_move
    if c_p == 1:
        print(f'#{m+1} 0')
        fuel_tank = size_move
        refill_gas = 0
        now_pos = 0
    else:
        print(f'#{m+1} {refill_gas}')
        fuel_tank = size_move
        refill_gas=0
        now_pos=0