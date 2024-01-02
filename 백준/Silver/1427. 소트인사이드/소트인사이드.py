num = int(input())
nlist = []
def solution():
    for i in str(num):
        nlist.append(int(i))
    nlist.sort(reverse=True)
    for j in nlist:
        print(j, end='')

solution()