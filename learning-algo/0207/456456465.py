arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binarySearch(arr, N, key):
    start = 0
    end = N - 1
    cnt = 0

    while start <= end : # 검색 구간이 남아있으면(Start > End가 아니라면)
        middle = (start + end) // 2

        if arr[middle] == key:
            # 검색 성공
            return cnt
        elif arr[middle] > key:
            end = middle - 1
            cnt += 1
        else:
            start = middle + 1
            cnt += 1
# return False    # 검색 실패


print(binarySearch(arr, len(arr), 3))
