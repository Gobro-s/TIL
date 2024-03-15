def solution(balls, share):
    answer = 0
    bunja = 1
    bunmo = 1
    for i in range(share):
        bunja *= balls-i
    for j in range(share):
        bunmo *= share-j
    answer += bunja/bunmo
    return answer