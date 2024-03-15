def solution(numbers):
    maximum = -100000000
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] * numbers[j] > maximum:
                maximum = numbers[i] * numbers[j]
    return maximum
