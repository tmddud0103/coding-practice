import sys
sys.stdin = open('input.txt')

# 전체 방식 중에서 2와 1의 갯수만 신경 썼다
# 안그러면 런타임 에러가 떠서
#여기서는 2, 1의 갯수에만 신경을 쓴 케이스를 도출하고
# 실제 계산에서 갯수를 이용해 전체 경우의 수를 계산하는 방법으로 하겠다
def dfs():
    temp_case = []
    case = []
    global max_number
    while sum(temp_case) + 2 <= max_number:
        temp_case.append(2)
    if max_number > sum(temp_case):
        temp_case.append(1)
    case.append(temp_case[:])
    while temp_case:
        while len(temp_case) > 0 and temp_case[-1] == 1:
            temp_case.pop()
        if len(temp_case) > 0 and temp_case[-1] == 2:
            temp_case.pop()
            temp_case.append(1)
            temp_case.append(1)
            while sum(temp_case) < max_number:
                temp_case.append(1)
        case.append(temp_case[:])
    case.pop()
    return case

# 팩토리얼 계산하는 def
def factorial(n):
    total = 1
    for i in range(n, 0, -1):
       total *= i
    return total

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    max_number = N // 10
    number_list = []
    matrix = dfs()
    count = 0
    for i in range(0, len(matrix)):
        multi_count = 0
        count1 = 0
        count2 = 0
        # count1 = 1의 갯수
        # count2 = 2의 갯수
        # multi_count 숫자가 2라면 2*2박스, 1*2 박스 세로로 2개
        # 2가지의 경우의 수가 있다
        # 2의 갯수만큼 제곱을 해주면 된다
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                count2 += 1
                multi_count += 1
            else:
                count1 += 1
        # 2와 1로 이루어진 리스트의 경우의 수
        # 2가 n개, 1이 m개 총합 n+m이라면
        # (n+m)! / (n! + m!)
        number_of_cases = int(factorial(len(matrix[i]))/(factorial(count1) * factorial(count2)))
        # 얘가 상당히 복잡한데
        # 여백이 좁아서 증명을 하진 않겠다
        count += 1 * (2 ** multi_count) * number_of_cases
    print(f'#{tc} {count}')