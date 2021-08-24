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

    return result

def min():
    global min_num
    for i in range(len(lists)):
        count = 0
        for j in range(N):
            count += matrix[j][lists[i][j]]
            if count > min_num:
                break
        if count < min_num:
            min_num = count
    return min_num

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    matrix = []
    check = [0] * N
    temp = []
    a = []
    for i in range(N):
        temp = list(map(int, input().split()))
        matrix.append(temp)
    min_num = 0
    for i in range(N):
        min_num += matrix[i][i]
        a.append(i)
    lists = perm(a)
    print(lists)
    # min()
    print(result)
    print('#{} {}'.format(tc, min_num))
    # 이 방법은 망했음ㄴ