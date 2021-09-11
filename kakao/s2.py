info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    score = []

    for i in range(len(info)):
        score.append([int(info[i].split()[-1]),i])
    print(sorted(score))
    for i in range(len(query)):
        count = 0

        target = int(query[i].split()[7])
        start = 0
        end = len(score)-1
        while start < end:
            mid = (start + end) // 2
            if score[mid][0] == target:
                start = end
            elif score[mid][0] < target:
                start = mid - 1
            else:
                end = mid +1
            print(mid, start, end)
        for j in range(mid+1):

            if query[i].split()[0] == '-' or info[score[j][1]].split()[0] == query[i].split()[0]:
                if query[i].split()[2] == '-' or info[score[j][1]].split()[1] == query[i].split()[2]:
                    if query[i].split()[4] == '-' or info[score[j][1]].split()[2] == query[i].split()[4]:
                        if query[i].split()[6] == '-' or info[score[j][1]].split()[3] == query[i].split()[6]:
                            count += 1
        answer.append(count)
    return answer


print(solution(info, query))
