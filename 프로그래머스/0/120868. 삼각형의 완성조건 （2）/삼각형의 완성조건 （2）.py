def solution(sides):
    answer = 0
    max_side = max(sides)
    min_side = min(sides)
    
    # max_sides이 가장 길 경우
    for new_side in range (max_side - min_side + 1, max_side + 1):
        answer += 1
        
    # 새로운 변(new_side)가 가장 길 경우
    for new_side in range (max_side + 1, max_side + min_side):
        answer += 1
        
    return answer