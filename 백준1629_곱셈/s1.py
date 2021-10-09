import sys

def power(A, B):
    global C
    if B == 1:
        return A % C
    temp = power(A, B // 2)
    if B % 2 == 0:
        return (temp * temp) % C
    return (temp * temp * A) % C



A, B, C = map(int, input().split())

print(power(A, B))