import sys
sys.stdin = open('input.txt')

def getMatch(N):
    m = len(N)
    pi = [0] * m
    j = 1
    for i in range(2, m):
        pi[i] = j
        j+=1
    return pi


N = sys.stdin.readline().rstrip()
M = sys.stdin.readline().rstrip()
S = sys.stdin.readline().rstrip()
PN = ''
PN += 'IO'*int(N) + 'I'
pi = getMatch(PN)
lenPN = len(PN)
cnt = 0
begin = 0
match = 0
while begin < int(M)-lenPN:
    if match<lenPN and PN[match] == S[match + begin]:
        match += 1
        if match == lenPN:
            cnt += 1
    else:
        if match == 0:
            begin += 1
        else:
            begin += match - pi[match - 1]
            match = pi[match - 1]

print(cnt)