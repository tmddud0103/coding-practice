import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
hip = []
for _ in range(N):
    i = int(sys.stdin.readline().rstrip())

    if i == 0:
        if len(hip) == 0:
            print(0)
            continue
        else:
            print(hip.pop())
            continue
    else:
        # if len(hip) == 1:
        #     hip.insert(0, i)
        # else:
        #     for j in range(0, len(hip)-1):
        #         if hip[j] >= i >= hip[j+1]:
        #             hip.insert(j+1, i)
        #             break
        s = 0
        e = len(hip) - 1
        if e == -1:
            hip.append(i)
            continue
        while True:
            mid = (s + e) // 2
            if s == mid:
                if i >= hip[e]:
                    pos_a = e + 1
                    break
                if i >= hip[mid]:
                    pos_a = mid + 1
                    break
                if i < hip[mid]:
                    pos_a = mid
                    break
            if i >= hip[mid]:
                s = mid
            else:
                e = mid
        hip.insert(pos_a, i)


