def solution(n):
    i = 3
    while i <= n-1:
        if n%i == 1:
            break
        i+= 1
    return i




print(solution(12))