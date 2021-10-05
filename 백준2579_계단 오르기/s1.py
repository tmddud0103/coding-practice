import sys
sys.stdin = open('input.txt')

stairs = int(sys.stdin.readline().rstrip())
p = [0]
s1 = [0]*(stairs+4)
s2 = [0]*(stairs+4)
for _ in range(stairs):
    p.append(int(sys.stdin.readline().rstrip()))
if stairs >= 1:
    s1[1] = p[1]
if stairs >= 2:
    s2[2] = p[2]
    s1[2] = p[1] + p[2]
if stairs >= 3:
    s1[3] = s2[2] + p[3]
    s2[3] = s1[1] + p[3]
if stairs >= 4:
    for i in range(4, stairs+1):
        s1[i] = s2[i-1]+p[i]
        s2[i] = max(s1[i-2], s2[i-2])+p[i]
print(max(s1[stairs], s2[stairs]))