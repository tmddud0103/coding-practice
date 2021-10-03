import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
dict_name = {}
answer = []
for _ in range(N):
    dict_name[sys.stdin.readline().rstrip()] = 1
for _ in range(M):
    temp = sys.stdin.readline().rstrip()
    if temp in dict_name.keys():
        answer.append(temp)
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])
