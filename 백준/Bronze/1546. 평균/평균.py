import sys
n = int(sys.stdin.readline().rstrip())
score = list(map(int, sys.stdin.readline().rstrip().split()))
max_score = max(score)
new_score = []
for i in score:
    new_score.append(i/max_score*100)
avr = sum(new_score)/n
print(avr)

