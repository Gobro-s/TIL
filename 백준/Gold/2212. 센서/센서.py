N = int(input())
K = int(input())

arr = list(map(int, input().split()))
arr.sort()

if K == 1:    
    print(arr[len(arr)-1] - arr[0])
    
elif K >= N:
    print(0)

else:
    dp = []
    for i in range(1, N):
        dp.append(arr[i]-arr[i-1])
    
    dp.sort()
    answer = 0
    for i in range(len(dp)-K+1):
        answer += dp[i]
    print(answer)