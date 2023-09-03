arr = [[0] for _ in range(9)]

for i in range(9):
    arr[i] = list(map(int, input().split()))

# print(arr) # [[],[],[]...] 형태로 input()

# 0 혹은 양수만 입력되므로 최댓값을 -1로 초기 설정
mx = -1
# 행, 열 == 0부터 시작
X = 0
Y = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > mx:  # 만약 arr의 [i]행 [j]열이 최댓값보다 크다면
            mx = arr[i][j]  # mx에 새로운 최댓값을 할당
            X = i+1         # 그때의 index(i) + 1
            Y = j+1         # 그때의 index(j) + 1

print(mx)
print(X, Y, end = '')