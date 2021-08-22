###### 문제 설명

n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다. n명이 사람을 줄을 서는 방법은 여러가지 방법이 있습니다. 예를 들어서 3명의 사람이 있다면 다음과 같이 6개의 방법이 있습니다.

- [1, 2, 3]
- [1, 3, 2]
- [2, 1, 3]
- [2, 3, 1]
- [3, 1, 2]
- [3, 2, 1]

사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return하는 solution 함수를 완성해주세요.

###### 제한사항

- n은 20이하의 자연수 입니다.
- k는 n! 이하의 자연수 입니다.

------

##### 입출력 예

| n    | k    | result  |
| ---- | ---- | ------- |
| 3    | 5    | [3,1,2] |

##### 입출력 예시 설명

입출력 예 #1
문제의 예시와 같습니다.





```python
def solution(n, k):
    a = [x for x in range(1, int(n) + 1)]
    length = len(a)
    
    if length == 1:
        return [a]
    else:
        result = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            for j in solution(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
    answer = result[k-1]
    return answer
```

```
TypeError: solution() missing 1 required positional argument: 'k'

테스트 결과 (~˘▾˘)~
1개 중 0개 성공
```

아니 대체 왜???????????