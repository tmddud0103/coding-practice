arr = [1, 2, 3]
N = len(arr)
sel = [0] * N

def powerset(idx):
    if idx == N:
        for i in range(N):
            if sel[i] == 1:
                print(arr[i], end=' ')
        print()
        return

    # sel 배열의 index 자리를 1로 바꾼다
    # => 해당 원소를 뽑았다!
    sel[idx] = 1
    # 다음 경우의 수로 진입
    powerset(idx + 1)

    # sel 배열의 index 자리를 0으로 바꾼다
    # => 해당 원소를 뽑지 않은 경우!
    sel[idx] = 0
    # 다음 경우의 수로 진입
    powerset(idx + 1)

powerset(0)