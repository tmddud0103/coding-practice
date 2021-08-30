import sys
sys.stdin = open('input.txt')

def male(sw):
    global switch
    for j in range(len(switch)):
        if (j+1) % sw == 0:
            if switch[j] == 1:
                switch[j] = 0
            else:
                switch[j] = 1

def female(sw):
    global switch
    i = 0
    while sw-i-1 >= 0 and sw+i-1 < len(switch) and switch[sw+i-1] == switch[sw-i-1]:
        i += 1
    i -= 1
    if i == -1:
        if switch[sw-1] == 1:
            switch[sw-1] = 0
        else:
            switch[sw-1] = 1
    else:
        for j in range(-i, i+1):
            sw1 = sw-1+j
            if switch[sw1] == 1:
                switch[sw1] = 0
            else:
                switch[sw1] = 1

N = int(input())
switch = list(map(int, input().split()))
students = int(input())
for student in range(students):
    sex, no_of_sw = list(map(int, input().split()))
    if sex == 1:
        male(no_of_sw)
    else:
        female(no_of_sw)
print(switch)
for i in range(len(switch)-1):
    print(switch[i], end = ' ')
print(switch[len(switch)-1])