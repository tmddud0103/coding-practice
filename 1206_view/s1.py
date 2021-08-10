import sys
sys.stdin = open('input.txt')

# test_case = int(input())
# 4개의 수에서 가장 큰 값을 출력하는 함수
def who_is_biggest(a, b, c, d):
    biggest_number = 0
    if (a >= b) and (a >= c) and (a >= d):
        biggest_number = a
    elif (b >= a) and (b >= c) and (b >= d):
        biggest_number = b
    elif (c >= a) and (c >= b) and (c >= d):
        biggest_number = c
    else:
        biggest_number = d
    return biggest_number

# 테스트 케이스는 10개
test_case = 10
for tc in range(1, test_case + 1):
    # 조망권이 있는 집은 우리가 사고 싶은 집이 아닐까 해서
    # 우리가 사고 싶은 층(집)이라고 변수명 정의
    we_want_buy_that_floor = 0
    number_of_buildings = int(input())
    floors_of_buildings = list(map(int, input().split()))
    for i in range(2, number_of_buildings - 2):
        #한 위치를 기준으로로 좌우로 2칸씩 존재하는 빌딩들 중에 가장 높은 빌딩의 층수를 구한다
        biggest_building = who_is_biggest(floors_of_buildings[i-2], floors_of_buildings[i-1], floors_of_buildings[i+1], floors_of_buildings[i+2])
        # 만약 주위 2칸에 존재하는 가장 높은 빌딩이 현재 기준의 빌딩보다 크다면?
        # => 조망권 = 0
        # 반대로 현재 기준의 빌딩이 주위 2칸에 존재하는 가장 높은 빌딩보다 크다면?
        # => 조망권이 존재한다
        # 얼마나 존재하는가? => 현재 기준 빌딩의 크기 - 주위 2칸 중에 가장 높은 빌딩
        if floors_of_buildings[i] > biggest_building:
            we_want_buy_that_floor += floors_of_buildings[i] - biggest_building
    print('#{} {}'.format(tc, we_want_buy_that_floor))