# backtracking

def f(i, k, s, key):     # 
    global cnt
    global c
    
    c += 1
    if s==key:
        cnt += 1
        return

    elif i == k or s > key:   # 다 더해도 key가 아니네? 아니면 이미 key를 넘었네?
        return                # 그럼 더 할 필요 없으니 그냥 return 해
    else:
        f(i+1, k, s, key)      # A[i] 미포함
        f(i+1, k, s+A[i], key) # A[i] 포함
        return


A = [i for i in range(1, 11)]
N = 10
key = 10
cnt = 0
c = 0

f(0, N, 0, key)
print(cnt, c)