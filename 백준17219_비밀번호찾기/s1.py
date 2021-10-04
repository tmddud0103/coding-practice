import sys
sys.stdin = open('input.txt')

N, M = sys.stdin.readline().split()
N, M = int(N), int(M)
dict = {}
for _ in range(N):
    key, value = sys.stdin.readline().split()
    dict[key] = value
for _ in range(M):
    print(dict[sys.stdin.readline().rstrip()])