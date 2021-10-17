import sys
sys.stdin = open('input.txt')

TC = int(sys.stdin.readline().lstrip())
for _ in range(TC):
    nn = list(map(str, sys.stdin.readline().rstrip()))
    n = int(sys.stdin.readline().lstrip())
    llist = str(sys.stdin.readline().rstrip())
    llist = llist.strip("[").strip("]").split(',')
    if n == 0:
        llist = []
    else:
        for i in range(len(llist)):
            llist[i] = int(llist[i])
    k = 0
    for rd in nn:
        if rd =='R':
            k+=1
        else:
            if n!=0:
                if k%2==0:
                    llist.pop(0)
                else:
                    llist.pop(-1)
                n-=1
            else:
                n = -1
                print('error')
                break
    if n == -1:
        pass
    elif n==0:
        print('[]')
    else:
        if k%2 == 1:
            llist.reverse()
        print('[', end='')
        for i in range(len(llist)-1):
            print(llist[i],end=',')
        print(llist[-1], end=']')
        print()





