arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(0, (1<<n)):       # 1 << n: 부분집합의 개수
    for j in range(0, n):        # 원소의 수 만큼 비트를 비교함
        if i & (1<<j):           # i의 j번째 비트가 1이면 j번째 원소 출력
        # ↑ i의 j번 비트가 1인지 검사하는 코드
            print('%d'%arr[j], end='')
    print()