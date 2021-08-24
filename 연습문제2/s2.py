# 부분집합 중 합이 10인 부분집합을 출력
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(data)
sel = [0] * N
# 여기에 어팬드해서 출력해도 가능
# results = []

def powerset(idx):
    # 아직 부분집합을 다 찾지 못한 경우
    if idx < N:
        sel[idx] = 1
        powerset(idx + 1)
        sel[idx] = 0
        powerset(idx + 1)

    # 전체 길이를 다 확인한 경우
    else:
        total = 0
        for i in range(N):
            if sel[i] ==1:
                total += data[i]
        if total == 10:
            for i in range(N):
                if sel[i] == 1:
                    print(data[i], end = ' ')
            print()
        return

powerset(0)

# 플러닝
# 재귀를 시킬 당시에 1 -> 2로 갈때 1이 있는지 없는지(0의 값을 가지는지 1의 값을 가지는지) 에 대한 정보를 저장한 상대로 다음 반복을 시킨다
# 경우의 수를 대폭 줄일 수 있다!