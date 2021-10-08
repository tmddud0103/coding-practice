import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().lstrip())
x = list(map(int, sys.stdin.readline().split()))
a = sorted(list(set(x)))
dict = {str:i for i, str in enumerate(a)}
for i in range(len(x)):
    print(dict[x[i]], end=" ")
print()