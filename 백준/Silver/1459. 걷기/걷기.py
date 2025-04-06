X, Y, W, S = map(int, input().split())

if X > Y:
    X, Y = Y, X

if S >= 2 * W:
    # 대각선이 더 느리면 모두 직선으로
    print((X + Y) * W)
elif S < W:
    # 대각선이 모든 면에서 유리하면,
    # 짝수 차이면 모두 대각선, 홀수 차이면 마지막은 W로
    if (Y - X) % 2 == 0:
        print(Y * S)
    else:
        print((Y - 1) * S + W)
else:
    # 최대한 대각선으로, 나머지는 직선으로
    print(X * S + (Y - X) * W)
