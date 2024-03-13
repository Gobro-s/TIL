def solution(n, t):
    answer = n
    for segyun in range(t):
        answer *= 2
    return answer