import sys
s = sys.stdin.readline().rstrip()
alpha = list(range(97,123))

for i in alpha:
    print(s.find(chr(i)))