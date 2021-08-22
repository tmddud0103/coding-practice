import sys
import time
start = time.time()
sys.stdin = open('input.txt')
# r = y
# c = x
tc = int(input())

def asd(size, r, c, k):
    next_size = int(size/2)
    if size > 2:
        if r < next_size and c < next_size:
            k = asd(next_size, r, c, k)
        elif r < next_size and c >= next_size:
            k += next_size ** 2
            k = asd(next_size, r, c - next_size, k)
        elif r >= next_size and c < next_size:
            k += (next_size ** 2) * 2
            k = asd(next_size, r - next_size, c, k)
        else:
            k += 3 * (next_size ** 2)
            k = asd(next_size, r - next_size, c - next_size, k)

    if size == 2:
        if r == 1 and c == 1:
            k += 3
        elif r == 1 and c == 0:
            k += 2
        elif r == 0 and c == 1:
            k += 1
        else:
            pass
    return k

for t in range(1, tc+1):
    k = 0
    N, r, c = map(int, input().split())
    print(asd(2 ** N, r, c, k))
print("time :", time.time() - start)

