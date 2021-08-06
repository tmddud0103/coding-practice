# 완주하지 못한 선수(r)

###### 문제 설명

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

##### 입출력 예

| participant                                       | completion                               | return   |
| ------------------------------------------------- | ---------------------------------------- | -------- |
| ["leo", "kiki", "eden"]                           | ["eden", "kiki"]                         | "leo"    |
| ["marina", "josipa", "nikola", "vinko", "filipa"] | ["josipa", "filipa", "marina", "nikola"] | "vinko"  |
| ["mislav", "stanko", "mislav", "ana"]             | ["stanko", "ana", "mislav"]              | "mislav" |

##### 입출력 예 설명

예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.







## 방법1. remove 사용

```python
def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
# p와 p[:]의 차이 = p를 사용하게 되면 밑에 p.remove에서 삭제를 하면 for문이 정상적으로 작동하지 않는다
# 그렇기 때문에 p[:] (= p를 처음부터 끝까지 돌리는 새로운 list)를 사용함으로써 for문의 고장을 없앴다
    for i in p[:]:
        for j in c[:]:
            if i == j:
                p.remove(i)
                c.remove(i)
                continue
        continue
    answer = str(p[0])
    return answer

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
```

#### 문제점

#### 효율성 테스트 실패 -> 할 수 있을거 같은데 방법은 좀 더 생각해보자



## 방법2. loop

```python
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
```

#### 문제점

#### 런타임 에러 + 시간초과 -> recursive의 치명적인 단점



## 방법3. 정렬하고 비교

```python
def solution(participant, completion):

    participant_sorted = sorted(participant)
    completion_sorted = sorted(completion)

    for i in range(len(completion_sorted)):
        if participant_sorted[i] != completion_sorted[i]:
            return participant_sorted[i]

        # 알파벳 순서로 마지막 사람이 완주를 못했을 수 있으므로
    return participant_sorted[-1]
```

제일 베스트인 것 같다