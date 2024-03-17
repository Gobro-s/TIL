def solution(array):
    answer = 0
    s = ''.join(str(num) for num in array)
    for i in s:
        if i == str(7):
            answer += 1
    return answer