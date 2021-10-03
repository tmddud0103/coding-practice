import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

alpTOno = {}
for i in range(1, N+1):
    temp = sys.stdin.readline().rstrip()
    alpTOno[temp], alpTOno[str(i)] = i, temp
for _ in range(M):
    temp = sys.stdin.readline().rstrip()

    print(alpTOno[temp])

