# https://www.acmicpc.net/problem/15552

# 목적 : input()대신 sys.stdin.readline() 사용
import sys


T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)