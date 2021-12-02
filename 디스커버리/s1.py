total = []
mat = []
def d():
    if total[6] % total[2] == 0:
        total.append(total[6] // total[2])
        mat.append(total[:])
        print(total)
        total.pop()
def c(temp):
    temp1 = temp - 4
    if temp1 >= 0:
        for i in range(1, 10):
            if temp1 % i == 0 and temp1 // i != 0:
                total.append(i)
                total.append(temp1 // i)
                d()
                total.pop()
                total.pop()
def b():
    for i in range(1, 10):
        if total[0] + i < 10:
            total.append(i)
            total.append(total[0] + i)
            c(total[0] + i)
            total.pop()
            total.pop()

def a(asd):
    for i in range(1, 10):
        if asd % i == 0:
            total.append(i)
            total.append(asd//i)
            b()
            total.pop()
            total.pop()




for i in range(1, 10):
    total.append(i)
    temp = i + 2
    a(temp)
    total.pop()
print('안겹치는거')
for ma in mat:
    nma = list(set(ma))
    if len(nma) == 8:
        print(ma)
