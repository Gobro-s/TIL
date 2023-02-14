# import sys
#
# sys.stdin = open('sample_input.txt')

# 전체 테스트 케이스
T = int(input())

# T만큼 반복해서 로직을 수행
for tc in range(1, T + 1):
    # 전체 개수
    N = int(input())
    # 각 건물의 높이
    numbers = list(map(int, input().split()))

    # 최종 결과값
    result = 0
    # 모든 상황에 대한 최대 낙찻값
    for i in range(N):
        # i 번째의 최대 낙찻값
        max_height = len(numbers) - (i + 1) # '나'는 빼야 하므로(i+1)

        for j in range(i+1, len(numbers)):
            # i보다 큰 j 번째 찾기
            # 찾았다면 최대 낙차 -1
            if numbers[i] <= numbers[j]:
                max_height -= 1

            # 최종 낙찻값이 가장 큰 것 찾기
        if result < max_height:
                result = max_height

    print(f'#{tc} {result}')