import sys
sys.stdin = open('input.txt')
test_case = int(input())

for tc in range(1, test_case + 1):
    length = int(input())
    snail = []
    print('#{}'.format(tc))
    #달팽이 만들기
    for i in range(length):
        snail += [[0]*length]
    # 몇번을 반복할까?
    # 처음엔 length 만큼 이동
    # 두번째, 세번째에는 length - 1 만큼 이동
    # ...
    # 2n, 2n + 1 번째에는 length - n 만큼 이동
    # 그럼 홀수번 이동할지 짝수번 이동할지 어떻게 알 수 있을까?
    # 총 행렬에 있는 번호의 갯수는 n ** n
    # (n ** n) = n + (n-1) +(n-1) .... +1 + 1 = 짝수
    # 마지막 움직임은 x축 1번, y축 1번이 마지막이다
    # 그러면 n의 숫자와 상관없이 무적권 홀수번 움직인다는 것을 알 수 있다
    # n**n = n + 2 * (n - 1) + ... + 2 * (1)
    # 심지어 총 2n-1 번 움직인다
    save_number = 1
    current_location = [0, -1]
    for i in range(1, 2*length):
        # n번째 움직임에서 
        # n % 4 = 1 일 경우 좌 -> 우
        # n % 4 = 2 일 경우 위 -> 아래
        # n % 4 = 3 일 경우 우 -> 좌
        # n % 4 = 4 일 경우 아래 -> 위
        #로 각각의 이동방향이 정해진다
        if i % 4 == 1:
            for j in range(0, length - i // 2):
                current_location[1] += 1
                snail[current_location[0]][current_location[1]] = save_number
                save_number += 1
        elif i % 4 == 2:
            for j in range(0, length - i // 2):
                current_location[0] += 1
                snail[current_location[0]][current_location[1]] = save_number
                save_number += 1
        elif i % 4 == 3:
            for j in range(0, length - i // 2):
                current_location[1] -= 1
                snail[current_location[0]][current_location[1]] = save_number
                save_number += 1
        else:
            for j in range(0, length - i // 2):
                current_location[0] -= 1
                snail[current_location[0]][current_location[1]] = save_number
                save_number += 1
    for i in range(0, len(snail)):
        for j in range(0, len(snail[i])):
            print(snail[i][j], end=' ')
        print()
