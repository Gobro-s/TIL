import sys
sys.stdin = open("binaryserch_input.txt", "r")

def binarySearch(pages, key):
    l = 1
    r = pages
    cnt = 0
    while l <= r:  # 검색 구간이 남아있으면(Start > End가 아니라면)
        middle = int((l + r) // 2)
        if middle == key:  # 검색 성공
            return cnt

        elif middle > key:  #만약 middle 값이 찾는 key보다 크다면
            r = middle      # middle을 새로운 오른쪽 끝으로 지정해주고
            cnt += 1        # 횟수를 1회 추가한다.

        elif middle < key:  # 만약 middle값이 key 보다 작다면
            l = middle     # middle값을 새로운 왼쪽 끝으로 지정해주고
            cnt += 1       # 횟수를 1회 추가한다.
    # return False  # 검색 실패

T = int(input())
for test_case in range(1, T + 1):           # Testcase가 주어진다.
    P, A, B = map(int, input().split())     # P A B input
    cntA = binarySearch(P, A)               # A의 cnt 개수를 구해준다.
    cntB = binarySearch(P, B)               # B의 cnt 개수를 구해준다.

    def match(cntA, cntB):
        winner = ''
        if cntA > cntB:      # A가 크면 B 출력
            winner = 'B'

        elif cntA < cntB:    # B가 크면 A 출력
            winner = 'A'

        else:                # 그 외 못찾거나 비기는 경우
            winner = '0'
        return winner


    print(f'#{test_case} {match(cntA, cntB)}')