## 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이
## 존재하는지를 계산하는 함수를 작성해보자.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
sumlist = []
for i in range(1 << n):  # 1<<n : 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i & (1 << j):  # i의 j번 비트가 1인 경우
            sumlist.append(arr[j])

        if sum(sumlist) == 0:
            print(True)
        else:
            print(False)