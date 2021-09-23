import sys
sys.stdin = open('input.txt')

def get_min_cost(n):
    """
    n월까지의 최소 수영장 이용 가격을 구한다.
    (1일 / 1달 / 3달 이용권을 이용하는 경우)
    """
    if n == 0:
        return 0

    if costs[n]:
        return costs[n]

    # min_cost: n월에 1일 이용권 or 1달 이용권을 이용하는 경우의 최소 비용
    min_cost = get_min_cost(n - 1) + min(month, day * plans[n])

    # (n-2)월부터 n월까지 3달 이용권을 이용하는 경우와 비교하여, 더 작은 값을 구한다.
    if n >= 3:
        min_cost = min(min_cost, get_min_cost(n - 3) + quarter)

    costs[n] = min_cost  # 메모이제이션
    return min_cost


T = int(input())
for tc in range(1, T + 1):
    """
    day / month / quarter / year: 1일 / 1달 / 3달 / 1년 이용권 가격
    plans: 1월 ~ 12월 수영장 이용 계획
    minimum: 최소 지출 비용 (초기값: 1년 이용권 가격)
    """
    day, month, quarter, year = map(int, input().split())
    plans = [0] + [int(x) for x in input().split()]
    minimum = year

    # costs: 달별 누적 최소 가격 (n번 인덱스 값 = n월까지의 최소 이용 금액)
    costs = [0] * 13

    # 1년 이용권 vs (1일 + 1달 + 3달 이용권)
    minimum = min(minimum, get_min_cost(12))
    print("#{} {}".format(tc, minimum))