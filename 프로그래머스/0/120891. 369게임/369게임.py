def solution(order):
    answer = 0
    strorder = str(order)
    for i in range(len(strorder)):
        if int(strorder[i]) in [3, 6, 9]:
            answer += 1
    return answer