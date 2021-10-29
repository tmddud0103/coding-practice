import operator


def solution(genres, plays):
    answer = []
    dic = dict()
    dicli = dict()
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
            dicli[genres[i]].append([plays[i], -i])
        else:
            dic[genres[i]] = plays[i]
            dicli[genres[i]] = [[plays[i], -i]]
    sdict = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    print(sdict, len(sdict))
    # print(dicli)
    for i in range(len(sdict)):
        temp = sorted(dicli[sdict[i][0]], reverse=True)
        # print(temp)
        answer.append(-temp[0][1])
        if len(temp)>1:
            answer.append(-temp[1][1])
    return answer



genres=["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]
print(solution(genres, plays)) # 4130
genres=["classic", "pop", "classic", "classic", "pop", "classic"]
plays=[500, 600, 150, 800, 2500, 100]
print(solution(genres, plays))  # [4, 1, 3, 0]
genres=["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"]
plays=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solution(genres, plays))  # [0, 1, 2, 4]

print(solution(["classic", "pop", "classic", "classic", "classic"], [500, 1000, 400, 300, 200, 100])) # 0,2,1