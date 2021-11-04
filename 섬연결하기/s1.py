from queue import PriorityQueue

def solution(n, costs):
    mat = [[0]*n for _ in range(n)]
    cnt = [100000] * n
    check = [0]*n
    for cost in costs:
        i, j, k = cost
        mat[i][j], mat[j][i] = k, k
    check[0] = 1
    q = PriorityQueue()
    for i in range(n):
        if mat[0][i]!=0:
            q.put((mat[0][i], i))
    answer = 0

    while q:
        if sum(check) == n:
            break
        a, c = q.get()
        if check[c] == 0:
            check[c] = 1

            answer += a
            for i in range(n):
                if mat[c][i]!=0 and check[i]==0:
                    q.put((mat[c][i], i))

    return answer



n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]] # 4

print(solution(n, costs))
n = 5
costs =[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]] #15
print(solution(n, costs))
n = 5
costs =[[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] #8
print(solution(n, costs))
n = 4
costs =[[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] #9
print(solution(n, costs))
n = 5
costs =[[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] #104
print(solution(n, costs))
n = 6
costs =[[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]] #11
print(solution(n, costs))
n = 5
costs =[[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]] #6
print(solution(n, costs))
n = 5
costs =[[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]] #8
print(solution(n, costs))
n = 5
costs =[[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]] #8
print(solution(n, costs))
