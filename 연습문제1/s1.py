# 다른 방식의 풀이 = 답이 다르다 = 신경 쓰지말고 새로운 풀이로 답을 도출하자
# 원하는 답은 s2.py에 다시 만들도록 하겠음
asd = '2+3*4/5'
as1 = '(6+5*(2-8)/2)'
as2 = '3+4+5*6+7'
number = []
not_num = []
def asdf(asd):
    for i in range(0, len(asd)):
        try:
            print(int(asd[i]), end = ' ')
        except:
            if asd[i] ==')':
                # not_num.pop()
                while not_num[-1] != '(':
                    a = not_num.pop()
                    print(a, end =' ')
                not_num.pop()
            elif asd[i] == '*' or asd[i] == '/':
                while not_num[-1] == '*' or not_num[-1] == '/':
                    a = not_num.pop()
                    print(a, end=' ')
                not_num.append(asd[i])
            else:
                not_num.append(asd[i])
    for _ in range(len(not_num)):
        a = not_num.pop()
        print(a, end=' ')
    print()


asdf(asd)
asdf(as1)
asdf(as2)