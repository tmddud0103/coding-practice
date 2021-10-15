import sys
sys.stdin = open('input.txt')

def aaa(l):
    if l > n:
        result = " ".join(k)
        print(result)
        return
    for i in range(1, 7):
        k.append(str(i))
        aaa(l+1)
        k.pop()
def bbb(ll, l):
    if ll > n:
        result = " ".join(k)
        print(result)
        return
    for i in range(l, 7):
        k.append(str(i))
        bbb(ll + 1, i)
        k.pop()
def ccc(ll):
    if ll > n:
        result = " ".join(k)
        print(result)
        return
    for i in range(1, 7):
        if str(i) not in k:
            k.append(str(i))
            ccc(ll + 1)
            k.pop()

n, m = list(map(int, sys.stdin.readline().split()))
if m == 1:
    k = []
    aaa(1)
if m == 2:
    k = []
    bbb(1, 1)
if m == 3:
    k = []
    ccc(1)