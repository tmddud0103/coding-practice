def solution(n):
    base = reverse_ten_to_three(n)
    result = int(base,3)
    return result


def reverse_ten_to_three(n):
    base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        base += str(mod)
    return base




n1 = 45
n2 = 125
print(solution(n1))
print(solution(n2))