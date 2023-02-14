# ()()((()))
# ((()((((()()((()())((())))))


T = int(input())
for test_case in range(1, T+1):

    bracket = input()

    lst = []
    rlt = 1

    for i in bracket:
        if i == '(':
            lst.append(i)
            # print(lst)



        elif i == ')':
            if len(lst) == 0:
            # == if not lst :
                rlt = -1
                break

            elif (len(lst) != 0) and (lst[-1] == '('):
                lst.pop(-1)
                # print(lst)

    # rlt = len(lst)

    # if rlt == 0:
    #     print(1)
    # else:
    #     print(-1)

    if lst:
        rlt = -1
    print(f'#{test_case} {rlt}')