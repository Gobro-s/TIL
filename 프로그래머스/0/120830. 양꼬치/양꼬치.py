def solution(n, k):
    answer = 0
    service = 0
    service += n//10
    answer += 12000*n + 2000*(k-service)
    return answer