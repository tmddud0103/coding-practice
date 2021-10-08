from collections import deque
def solution(n, m, x, y, queries):
    q = deque([])
    q.append([x, y])
    for i in queries[::-1]:
        for j in range(i[1]+1):
            for _ in range(len(q)):
                print(q)
                a = q.popleft()
                if i[0] == 2:
                    if y == 0:
                        q.append([x, 0])
                        q.append([x, 1])
                    else:
                        q.append([x, y - 1])
                elif i[0] == 3:
                    if x == n - 1:
                        q.append([n - 1, y])
                        q.append([n - 2, y])
                    else:
                        q.append([x + 1, y])

                elif i[0] == 1:
                    if y == m - 1:
                        q.append([x, m - 1])
                        q.append([x, m - 2])
                    else:
                        q.append([x, y + 1])
                else:
                    if x == 0:
                        q.append([0, y])
                        q.append([1, y])
                    else:
                        q.append([x-1, y])
    result = []
    print(q)
    for value in q:
        if value not in result:
            result.append(value)
    print(result)
    return len(result)




n, m = 2, 5
x, y = 0, 1
queries = [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]
solution(n, m, x, y, queries)
# n, m = 2, 2
# x, y = 0, 0
# queries = [[2,1],[0,1],[1,1],[0,1],[2,1]]
# solution(n, m, x, y, queries)