# 아이디어
# n명의 사람이 있다
# n명의 사람에게 n개의 카드를 한장씩 나누어 주는 방법은 간단하다
# n!
# 그렇다면 싫어하는 숫자는 어떻게 처리할까
# 예시
# 3명의 사람이 각각 1, 2, 3을 싫어한다고 하자
# 3! - (1번이 1을 선택하는 경우의 수, 2번이 2를 선택하는 경우의 수, 3번이 3을 선택하는 경우의 수)
#       + (1,2 번이 각각 1, 2를 선택하는 경우의 수)*3 -(1,2,3번이 1,2,3을 선택하는 경우의 수)
#  = n(1합2합3) - (n(1) + n(2) + n(3)) + (n(1교2) + n(2교3) + n(3교1)) -n(1교2교3)
# 문제점 1 같은 숫자를 싫어할 경우 = 교집합이 0임을 생각하면 된다
# 문제점 2 n 밖에 있는 숫자를 싫어할 경우 = 그 사람은 교집합을 계산할 때 무시하면 된다
# 문제점 3 이 모든걸 코드로 작성 -> 해보자
import sys
sys.stdin = open('input.txt')

def perm(a):
    length = len(a)
    if length == 1:
        return [a]
    else:
        result = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            for j in perm(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
    print(result)
    return result

test_case = int(input())

for tc in range(1, test_case + 1):
    N = int(input())
    # N 명의 사람, N개의 숫자
    a = [x for x in range(1, int(N) + 1)]
    c = perm(a)
    total_cases = len(c)
    count = 0
    hate = list(map(int, input().split()))
    for i in range(0, len(c)):
        for j in range(N):
            if int(c[i][j]) == hate[j]:
                count += 1
                break
    print('#{} {}'.format(tc, total_cases - count))









    # for i in range(1 << N):
    #     sum_of_subset = 0
    #     subset = []
    #     for j in range(N + 1):
    #         if i & (1 << j):
    #             subset += [hate[j]]
    #     print(subset)