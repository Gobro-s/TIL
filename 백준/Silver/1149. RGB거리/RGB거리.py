N = int(input())

color = []

for _ in range(N):
  rgb = list(map(int, input().split()))
  color.append(rgb)

for i in range(1,N):
  color[i][0] = min(color[i-1][1], color[i-1][2]) + color[i][0]
  color[i][1] = min(color[i-1][0], color[i-1][2]) + color[i][1]
  color[i][2] = min(color[i-1][1], color[i-1][0]) + color[i][2]

print(min(color[N-1][0],color[N-1][1],color[N-1][2]))