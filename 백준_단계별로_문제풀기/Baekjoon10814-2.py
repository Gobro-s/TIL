N = int(input())
user = []

for _ in range(1, N+1):
    age, name = map(str, input().split())
    age = int(age)
    user.append((age, name))

user.sort(key = lambda x : x[0])

for i in user:
    print(i[0], i[1])


## 한자릿수 두자릿수 세자릿수 나이가 있을 수 있으므로
## 따로 받아줘야 한다.