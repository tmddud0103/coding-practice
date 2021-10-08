import sys
sys.stdin = open('input.txt')

import string

tmp = string.digits+string.ascii_lowercase

def convert(num, base):
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

def check(a, blist):
    lena = len(a)
    for b in blist:
        ck = 0
        for i in range(lena):
            if a[i] != b[i]:
                ck += 1
                if ck == 2:
                    break
        if ck == 1:
            return b


TC = int(input())

for tc in range(1, TC + 1):
    binary = list(input())
    triple = str(input())

    change_bin = []
    for i in range(1, len(binary)):
        if binary[i] == '1':
            binary[i] = '0'
            a = convert(int(''.join(binary), 2), 3)
            if len(a) == len(triple):
                change_bin.append(a)
            binary[i] = '1'
        else:
            binary[i] = '1'
            a = convert(int(''.join(binary), 2), 3)
            if len(a) == len(triple):
                change_bin.append(a)
            binary[i] = '0'
    print(change_bin)
    answer_tri = check(triple, change_bin)
    print('#{} {}'.format(tc, int(answer_tri, 3)))