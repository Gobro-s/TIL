import sys
sys.stdin = open("bracket_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    code = input()
    lst = []
    rlt = 0


    for i in code:
        if i == '(' or '{':
            lst.append(i)

        elif i == ')' or '}':
            if not lst:
                rlt = 0
                break

            elif lst and (lst[-1] == '(' or '{'):
                lst.pop(-1)


    if len(lst) != 0:
        rlt = -1
    print(f'#{test_case} {rlt}')