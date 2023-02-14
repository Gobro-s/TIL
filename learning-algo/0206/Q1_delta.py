T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    for i in range(1,N+1):
        for j in range(N):
            for di, dj in [[0,1], [1,0], [0,-1], [-1, 0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni <N and 0 <= nj < N:
                    # print(sum(abs(i+ni-i), abs(j+nj-j), abs(i-ni-i), abs(j-nj)))
                    print(i, j, ni, nj)
