def solution(before, after):
    answer = 0
    sortb = sorted(before)
    sorta = sorted(after)
    if sortb == sorta:
        answer += 1
    return answer