# stack 구현, 구현한 스택을 이용해 3개의 데이터를 스택에 저장,
# 다시 3번 꺼내서 출력해 봅니다.





stack = [0] * 3  # 리스트 3개
top = -1   # top의 초기값 -> 즉 top = -1 은 빈 스택

top += 1  # push(10)
stack[top] = 10

top += 1  # push(20)
stack[top] = 20

top += 1  # push(30)
stack[top] = 30

top -= 1
print(stack[top+1])

top -= 1
print(stack[top+1])

top -= 1
print(stack[top+1])