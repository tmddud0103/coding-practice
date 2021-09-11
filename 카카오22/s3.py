n=111111111111
k=2

def solution(n, k):
    rev_base = ''
    answer = 0
    if k == 10:
        rev_base = str(n)[::-1]
    elif k == 2:
        rev_base = str(bin(n)[2:])[::-1]
    elif k == 8:
        rev_base = str(oct(n)[2:])[::-1]
    else:
        while n > 0:
            n, mod = divmod(n, k)
            rev_base += str(mod)
    print(rev_base)
    check = ''
    rev_base = list(rev_base)
    for i in range(len(rev_base)-1, -1, -1):
        if rev_base[i] != '0':
            check += rev_base.pop(i)
        else:
            if check != '' and check != '1':
                ck = int(check)
                check = ''

                answer = prime(ck, answer)
            else:
                check = ''
    if check != '' and check != '1':
        ck = int(check)

        answer = prime(ck, answer)
    return answer

def prime(a, b):
    if a != 2 and a % 2 == 0:
        return b
    for i in range(3, a, 2):
        if a % i == 0:
            return b
    b += 1
    return b

print(solution(n, k))