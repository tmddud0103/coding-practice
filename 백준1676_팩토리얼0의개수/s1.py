x=1
cnt=0
n=int(input())

for i in range(1,n+1):
    x*=i

x=str(x)
for i in range(len(x)-1,-1,-1):

    if(x[i]=="0"):
        cnt+=1
    else:
        print(cnt)
        break