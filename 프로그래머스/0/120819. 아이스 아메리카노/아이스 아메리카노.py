def solution(money):
    answer = []
    coffee = money // 5500
    charge = money - coffee*5500
    answer.append(coffee)
    answer.append(charge)
    return answer