asd = [1, 2,3 ,4 ,5 ,6 ,7]
k = max(asd) #asd에서 최고 값
counts = [0]* (k+1) # 카운트 하려고 만듬
data = [0, 1, 2, 3, 4, 5, 6, 7, 8] # k를 이용해도 됐는데, 귀찮아서 그냥 씀 얘를 이용해서 몇번째 데이터인지 확인
temp = [0] *(len(asd)) # 저장용도, 답 도출

for i in range(0, len(asd)):
    counts[asd[i]] += 1
print(counts)

for i in range(1, len(counts)):
    counts[i] += counts[i-1]
print(counts) #진짜 카운트

for i in range(len(asd)-1, -1, -1):
    counts[asd[i]] -= 1
    temp[counts[asd[i]]] = asd[i]
    print('counts', counts)
    print(temp)