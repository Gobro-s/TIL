def solution(dots):
    answer = 0
    w = max(dots)[0] - min(dots)[0]
    h = max(dots)[1] - min(dots)[1]
    answer += w*h
    return answer