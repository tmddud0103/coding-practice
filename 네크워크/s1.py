def solution(n, computers):
    check = [0]*n
    answer = 0
    q = []
    for i in range(n):
        if check[i] == 0:
            q.append(i)
            check[i] = 1
            while q:
                a = q.pop()
                for j in range(n):
                    if computers[a][j] == 1 and check[j] == 0:
                        check[j] = 1
                        q.append(j)
            answer += 1
    return answer