# https://www.acmicpc.net/problem/2605

N = int(input())
student = list(map(int, input().split()))
result = []
for idx, stu in enumerate(student, 1):
    result.insert((idx-1)-stu, idx)

for j in result:
    print(j, end = " ")