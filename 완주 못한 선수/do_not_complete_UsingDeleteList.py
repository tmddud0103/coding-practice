def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    for i in p[:]:
        for j in c[:]:
            if i == j:
                p.remove(i)
                c.remove(i)
                continue
        continue
    answer = str(p[0])
    return answer






part1 = ["leo", "kiki", "eden"]
comp1 = ["eden", "kiki"]

part2 = ['mariana', 'josipa', 'nikola', 'vinko', 'fili']
comp2 = ['josipa', 'fili', 'mariana', 'nikola']

part3 = ["mislav", "stanko", "mislav", "ana"]	
comp3 = ["stanko", "ana", "mislav"]

print(solution(part1, comp1))
print(solution(part2, comp2))
print(solution(part3, comp3))