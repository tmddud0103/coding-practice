import sys
from collections import deque
sys.stdin = open('input.txt')

def LRstring(now, dire):
    x1 = now // 1000  # 1000 자리
    x2 = (now % 1000) // 100  # 100 자리
    x3 = (now % 100) // 10  # 10 자리
    x4 = now % 10
    if dire =="L":
        return x2 * 1000 + x3 * 100 + x4 * 10 + x1
    else:
        return x4 * 1000 + x1 * 100 + x2 * 10 + x3

def asd(q):
    global b, ch
    while q:
        now, spin = q.popleft()
        if now*2 >= 10000 and ch[(now*2)%10000]==0:
            if (now*2)%10000 == b:
                return spin+'D'
            ch[(now * 2) % 10000] = 1
            q.append([(now*2)%10000, spin+'D'])

        elif 1<=now*2 < 10000 and ch[(now*2)]==0:
            if (now*2) == b:
                return spin+'D'
            ch[(now * 2)] =1
            q.append([now * 2, spin + 'D'])

        temp = LRstring(now, "L")
        if temp == b:
            return spin + 'L'
        if ch[temp]==0:
            q.append([temp, spin+'L'])
            ch[temp] =1
        temp = LRstring(now, "R")
        if temp == b:
            return spin + 'R'
        if ch[temp] == 0:
            q.append([temp, spin + 'R'])
            ch[temp] = 1


        if now == 0 and ch[9999] == 0:
            if 9999 == b:
                return spin+'S'
            ch[9999] = 1
            q.append([9999, spin+'S'])
        elif now > 0 and ch[now-1] == 0:
            if now-1 == b:
                return spin+'S'
            ch[now-1] = 1
            q.append([now-1, spin+'S'])


TC =  int(sys.stdin.readline().lstrip())
for _ in range(TC):
    ch = [0]*10001
    a, b = map(int, sys.stdin.readline().split())
    q = deque([[a, '']])
    print(asd(q))
