# https://www.acmicpc.net/problem/2839

# 경우의 수
# 1. 5의 배수 == > N//5 봉지만 들고가
# 2. 5와 3으로 조합이 될 때
# 3. 3의 배수
# 4. 안될때

n = int(input())

if n % 5 == 0:  # 5으로 나눠떨어질 때
    print(n // 5)
else:
    p = 0
    while n > 0:
        n -= 3
        p += 1
        if n % 5 == 0:  # 3kg과 5kg를 조합해서 담을 수 있을 때
            p += n // 5
            print(p)
            break
        elif n == 1 or n == 2:  # 설탕 봉지만으로 나눌 수 없을 때
            print(-1)
            break
        elif n == 0:  # 3으로 나눠떨어질 때
            print(p)
            break
