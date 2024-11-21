import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    word = sys.stdin.readline().rstrip()
    print(word[0] + word[-1])