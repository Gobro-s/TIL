# https://www.acmicpc.net/problem/15596

def solve(n):
    sum_ = 0
    for i in n:
        sum_ += i
    return sum_

# 스택으로 풀어보기?

def solve_2(n):
    stack = list(n)
    result = ''
    top = -1
    while stack:
        if not stack:
            break
        else:
            stack.pop() + result
            result += stack.pop()
            return result
    
# 재귀로 풀어보기