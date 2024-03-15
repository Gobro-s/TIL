def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def solution(n):
    composite_count = 0
    for num in range(2, n + 1):
        if count_divisors(num) >= 3:
            composite_count += 1
    return composite_count