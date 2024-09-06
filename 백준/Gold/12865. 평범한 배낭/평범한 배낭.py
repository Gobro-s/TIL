import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

dp=[0 for _ in range(k+1)]
for W,V in arr:
   for j in range(k,W-1,-1):
      dp[j]=max(dp[j],dp[j-W]+V)

print(dp[k])