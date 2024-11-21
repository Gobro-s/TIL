import sys
for _ in sys.stdin:
    a, b = map(int, _.rstrip().split())
    print(a+b)
    