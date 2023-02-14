T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for test_case in range(1, T+1):
    N = map(int, input().split())
## 전제조건 : 달팽이는 시작지점에서 우, 하, 좌, 상 방향 순으로 움직인다.
# 달팽이는 처음은 n칸 움직인다.
# 그 다음 두번은 n-1 만큼 움직인다.
# 그 다음 두번은 n-2 만큼 움직인다.
# 그 다음 두번은 n-3 만큼 움직인다.
    i = 0
    j = 0
    cnt = 0
    for i in range(N):
        if 0 <= cnt < 1:
            i + (n - x)
            cnt += 1
        elif 1 <= cnt <= 2:








