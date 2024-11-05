arr = [[] for _ in range(4)]
for i in range(4):
   tempArr = input()
   for j in range(len(tempArr)):
       arr[i].append(int(tempArr[j]))
k = int(input())
moves = []
for _ in range(k):
    a, b = map(int, input().split())
    moves.append((a, b))

def turn_right(array):
    right = array[7]
    for i in range(6, -1, -1):
        array[i + 1] = array[i]
    array[0] = right

def turn_left(array):
    left = array[0]
    for i in range(0, 7):
        array[i] = array[i + 1]
    array[7] = left

for x in range(k):
    num, dir = moves[x]
    num -= 1 # index 맞추기 위함
    flagLeft = arr[num][6]
    flagRight = arr[num][2]
    if dir == 1:
        turn_right(arr[num])
    else:
        turn_left(arr[num])
    tempDir = dir
    tempFlagLeft = flagLeft
    tempFlagRight = flagRight
    for i in range(num-1, -1, -1):
        if tempFlagLeft != arr[i][2]:
            if tempDir == 1:
                tempFlagLeft = arr[i][6]
                tempFlagRight = arr[i][2]
                turn_left(arr[i])
                tempDir *= -1
            else:
                tempFlagLeft = arr[i][6]
                tempFlagRight = arr[i][2]
                turn_right(arr[i])
                tempDir *= -1
        else:
            break
    tempDir = dir
    tempFlagLeft = flagLeft
    tempFlagRight = flagRight
    for i in range(num + 1, 4):
        if tempFlagRight != arr[i][6]:
            if tempDir == -1:
                tempFlagLeft = arr[i][6]
                tempFlagRight = arr[i][2]
                turn_right(arr[i])
                tempDir *= -1
            else:
                tempFlagLeft = arr[i][6]
                tempFlagRight = arr[i][2]
                turn_left(arr[i])
                tempDir *= -1
        else:
            break

ans = 0
for i in range(len(arr)):
    if arr[i][0] == 1:
        if i == 0:
            ans += 1
        elif i == 1:
            ans += 2
        elif i == 2:
            ans += 4
        else:
            ans += 8
print(ans)