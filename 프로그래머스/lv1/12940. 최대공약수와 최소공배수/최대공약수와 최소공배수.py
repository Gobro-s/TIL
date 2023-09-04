def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if not n%i and not m%i:
            answer.append(i)
            break
    for j in range(max(n, m), (n*m)+1):
        if not j%n and not j%m:
            answer.append(j)
            break
    return answer