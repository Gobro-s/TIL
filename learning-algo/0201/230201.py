#box[i]의 오른쪽, box[i+1] ~ box [N-1]

# N = int(input())
# arr = list(map(int, input().split()))
# for i in range(N-1, 0, -1):  # 각 구간의 끝
#     for j in range(i):     # 비교할 왼쪽 원소
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]  # 큰 원소를 오른쪽으로
# print(*arr)


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[0]   # 첫 원소를 최대로 가정
    for i in range(1, N):  # 나머지 원소와 비교
        if maxV < arr[i]:
            maxV = arr[i]
    print(f'#{tc} {maxV}')
    