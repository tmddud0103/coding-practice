def solution(s):
    count_p = 0
    count_y = 0
    for word in s:
        if word == 'p' or word == 'P':
            count_p += 1
        if word == 'y' or word == 'Y':
            count_y += 1
    if count_p == count_y:
        return True
    return False


s1 = "pPoooyY"
s2 = "Pyy"
print(solution(s1))
print(solution(s2))