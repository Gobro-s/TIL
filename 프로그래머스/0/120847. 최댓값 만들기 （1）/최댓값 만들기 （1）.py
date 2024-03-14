def solution(numbers):
    answer = 0
    maximum = max(numbers)
    numbers.remove(maximum)
    second = max(numbers)
    answer += maximum * second
    return answer