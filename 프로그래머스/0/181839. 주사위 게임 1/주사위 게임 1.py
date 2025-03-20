def solution(a, b):
    answer = 0
    if a%2 and b%2:
        answer += a**2 + b **2
    elif a%2 and b%2==0:
        answer += (a+b)*2
    elif b%2 and a%2==0:
        answer += (a+b)*2
    elif a%2==0 and b%2==0:
        answer += abs(a-b)
    return answer