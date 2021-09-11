board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]




def solution(board, skill):
    answer = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            deff = board[i][j]
            for k in range(len(skill)):
                if skill[k][1] <= i <= skill[k][3] and skill[k][2] <= j <= skill[k][4]:
                    if skill[k][0] == 1:
                        deff -= skill[k][5]
                    else:
                        deff += skill[k][5]
            if deff > 0:
                answer += 1
    return answer



print(solution(board, skill))