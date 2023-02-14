import sys
sys.stdin = open("input.txt", "r")


T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
N = len(A)


sublist = []
for i in range(1<<N):
	# j: arr의 idx
    list_a = []
    for j in range(N):
    	if i & (1 << j):
            list_a.append(A[j])
    sublist.append(list_a)

    print(sublist)