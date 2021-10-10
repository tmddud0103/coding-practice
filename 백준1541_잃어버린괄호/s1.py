import sys
sys.stdin = open('input.txt')
a = list(map(str, sys.stdin.readline()))
b = []
temp = ''
for i in range(len(a)):
    if a[i] == '-' or a[i] == '+':
        b.append(int(temp))
        b.append(a[i])
        temp = ''
    else:
        temp += a[i]
b.append(int(temp))
total = b[0]
i = 1
while i < len(b):
    if b[i] == '+':
        total += b[i+1]
        i += 2
    elif i+3 < len(b):
        temp = 0
        i += 1
        while i < len(b)-1 and b[i+1] != '-':
            temp += b[i]
            i += 2
        temp += b[i]
        i += 1
        total -= temp
    else:
        total -= b[i+1]
        i += 2
print(total)