def solution(i, j, k):
    cnt = 0
    for num in range(i, j + 1):
        cnt += str(num).count(str(k))
    return cnt