def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    try: 
        if p[0] == c[0]:
            p.remove(p[0])
            c.remove(c[0])
            return solution(p, c)
        else:
            return p[0]


    except IndexError:
        return p[0]

#밑에 input은 공통으로 들어가야 돌아가는지 안돌아가는지 확인이 가능하다
part1 = ["leo", "kiki", "eden"]
comp1 = ["eden", "kiki"]

part2 = ['mariana', 'josipa', 'nikola', 'vinko', 'fili']
comp2 = ['josipa', 'fili', 'mariana', 'nikola']

part3 = ["mislav", "stanko", "mislav", "ana"]	
comp3 = ["stanko", "ana", "mislav"]

print(solution(part1, comp1))
print(solution(part2, comp2))
print(solution(part3, comp3))