import sys
sys.stdin = open("flat_input.txt", "r")


'''
가로 길이는 항상 100으로 주어진다.

모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.

덤프 횟수는 1이상 1000이하로 주어진다.

주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 
그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).
'''
T = 10 #10회의 테스트 케이스
for test_case in range(1, T+1):
    dump = int(input())  # 덤프 횟수
    height = list(map(int, input().split())) #높이

    i = 0
    while i < dump:
        height[height.index(max(height))] -= 1
        height[height.index(min(height))] += 1

        if max(height) - min(height) <= 1:
            break
        i += 1

    print(f'#{test_case} {max(height) - min(height)}')