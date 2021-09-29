import sys
sys.stdin = open('input.txt')

N = list(map(str, input()))
bit = ''
for i in N:
    if i in '0123456789':
        a = str(format(int(i), 'b'))
        while len(a) != 4:
            a = '0' + a
        bit += a
    else:
        if i == 'A':
            a = str(format(10, 'b'))
            bit += a
        elif i == 'B':
            a = str(format(11, 'b'))
            bit += a
        elif i == 'C':
            a = str(format(12, 'b'))
            bit += a
        elif i == 'D':
            a = str(format(13, 'b'))
            bit += a
        elif i == 'E':
            a = str(format(14, 'b'))
            bit += a
        elif i == 'F':
            a = str(format(15, 'b'))
            bit += a
        else:
            pass
k = 0
ans = ''
while k != len(bit):
    if k + 5 < len(bit):
        if bit[k : k + 6] == '001101':
            ans += '0'
            k += 5
        elif bit[k: k + 6] == '010011':
            ans += '1'
            k += 5
        elif bit[k: k + 6] == '111011':
            ans += '2'
            k += 5
        elif bit[k: k + 6] == '110001':
            ans += '3'
            k += 5
        elif bit[k: k + 6] == '100011':
            ans += '4'
            k += 5
        elif bit[k: k + 6] == '110111':
            ans += '5'
            k += 5
        elif bit[k: k + 6] == '001011':
            ans += '6'
            k += 5
        elif bit[k: k + 6] == '111101':
            ans += '7'
            k += 5
        elif bit[k: k + 6] == '011001':
            ans += '8'
            k += 5
        elif bit[k: k + 6] == '101111':
            ans += '9'
            k += 5
        else:
            pass
    k += 1
print('ans', ans)