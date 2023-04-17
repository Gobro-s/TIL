n = int(input())

bee = 1  # 벌의 출발지
cnt = 1  # 바퀴(두께)수
while n > bee:
    bee += 6 * cnt  # 벌집은 6n으로 증가
    cnt += 1

print(cnt)
