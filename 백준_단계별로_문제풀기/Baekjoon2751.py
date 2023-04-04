N = int(input())

lst=[]
for i in range(1, N+1):
    lst.append(int(input()))

lst.sort()
print(*lst, sep='\n')