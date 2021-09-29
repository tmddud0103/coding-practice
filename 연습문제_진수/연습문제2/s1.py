import sys
sys.stdin = open('input.txt')

N = list(map(str, input()))
bit = ''
answer = []
for i in range(len(N)):
    if N[i] in '01234567':
        a = str(format(int(N[i]), 'b'))
        while len(a) != 4:
            a = '0' + a
        bit += a
    elif N[i] in '89':
        a = str(format(int(N[i]), 'b'))
        bit += a
    else:
        if N[i] == 'A':
            a = str(format(10, 'b'))
            bit += a
        elif N[i] == 'B':
            a = str(format(11, 'b'))
            bit += a
        elif N[i] == 'C':
            a = str(format(12, 'b'))
            bit += a
        elif N[i] == 'D':
            a = str(format(13, 'b'))
            bit += a
        elif N[i] == 'E':
            a = str(format(14, 'b'))
            bit += a
        elif N[i] == 'F':
            a = str(format(15, 'b'))
            bit += a
        else:
            pass

j=0
for i in range(len(bit)//7):
    j+=1
    temp = bit[0 + i * 7: 7 + i * 7]
    answer.append(int(temp, 2))
answer.append(int(bit[j*7], 2))
print(answer)