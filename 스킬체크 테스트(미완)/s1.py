import sys
sys.stdin = open('input.txt')

n, k = list(map(int, input().split()))

def solution(a):
    length = len(a)
    if length == 1:
        return [a]
    else:
        result = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            for j in solution(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
        return result

a = [x for x in range(1, int(n) + 1)]
print(solution(a)[k-1])