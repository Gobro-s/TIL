N = 10
M = 3

for i in range(N-M+1):
    for j in range(i+1, N-M+2):
        for k in range(j+1, N-M+3):
            print(i, j, k)