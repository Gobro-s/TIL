while True:
    lst = list(map(int, input().split()))
    lst.sort()
    bitbyun = lst[-1]
    if sum(lst) == 0:
        break
    elif lst[0]**2 + lst[1]**2 == lst[-1]**2:
        print('right')
    else:
        print('wrong')
