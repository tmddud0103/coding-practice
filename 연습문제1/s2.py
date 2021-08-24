asd = '2+3*4/5'
number = []
not_num = []
def asdf(asd):
    for i in range(0, len(asd)):
        try:
            print(int(asd[i]), end = ' ')
        except:
            not_num.append(asd[i])
    for _ in range(len(not_num)):
        a = not_num.pop()
        print(a, end=' ')
    print()


asdf(asd)