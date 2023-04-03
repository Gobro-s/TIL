lst = list(map(int, input().split()))
s_list = sorted(lst)
r_list = sorted(lst, reverse=True)

if lst == s_list:
    print('ascending')
elif lst == r_list:
    print('descending')
else:
    print('mixed')