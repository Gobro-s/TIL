def solution(numbers, direction):
    if direction == 'left':
        # 배열을 왼쪽으로 한 칸씩 회전
        return numbers[1:] + [numbers[0]]
    elif direction == 'right':
        # 배열을 오른쪽으로 한 칸씩 회전
        return [numbers[-1]] + numbers[:-1]
