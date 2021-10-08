def solution(n, left, right):
    a = []
    rl = right - left
    ln = left//n
    ln2 = left%n
    # [ln, ln2]
    for _ in range(rl+1):
        if ln2 == n:
            ln2 = 0
            ln += 1
        if ln > ln2:
            a.append(ln+1)
        else:
            a.append(ln2+1)
        ln2 += 1
    return a



print(solution(3, 2, 5))
# print(solution(3, 3, 5))
# print(solution(3, 4, 5))
print(solution(4, 7, 14))
# print(solution(5, 7, 14))
# print(solution(1, 0, 1))
# print(solution(2, 0, 3))