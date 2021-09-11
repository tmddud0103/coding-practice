id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    report = set(report)
    report = list(report)
    id_dict = dict.fromkeys(id_list, 0)
    id_dict2 = dict.fromkeys(id_list, [])
    for i in range(len(report)):


        a = id_dict2[report[i].split()[1]][:]
        a.append(report[i].split()[0])
        id_dict2[report[i].split()[1]] = a

    for key, value in id_dict2.items():
        if len(value) >= k:
            for i in value:
                id_dict[i] += 1
    answer =list(id_dict.values())



    return answer


print(solution(id_list, report, k))