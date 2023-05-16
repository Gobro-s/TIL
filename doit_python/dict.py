# 딕셔너리 형태 key=1, value='hi'
a = {1: 'hi'}

# Value에 리스트도 넣을 수 있다.
alist = {'a': [1, 2, 3]}

# 딕셔너리 쌍 추가하기
a[2] = 'bye'
print(a)  # {1: 'hi', 2: 'bye'}

a['name'] = 'pey'
print(a)  # {1: 'hi', 2: 'bye', 'name': 'pey'}

a[3] = [1, 2, 3]
print(a)  #  # {1: 'hi', 2: 'bye', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리를 사용하는 방법
sport = {'김연아' : '피겨스케이팅', '류현진': '야구', '손흥민': '축구', '하승진': '농구'}
# 딕셔너리 내의 key 들 출력
print(sport.keys())  # ['김연아', '류현진', '손흥민', '하승진']
# 딕셔너리 내의 value 들 출력
print(sport.values()) # ['피겨스케이팅, '야구', '축구', '농구']
# 딕셔너리에서 key를 사용해 value 얻기
print(sport['김연아']) # 피겨스케이팅
user = {'name': 'penny', 'phone': '01012345678', 'birth': '1111'}
print(user['name'])   # penny
print(user['phone'])  # 01012345678
print(user['birth'])  # 1111

## 딕셔너리 사용 시 key값 중복 X, Key는 list가 될 수 없다.

# key, values 쌍으로 받기
print(user.items())  # ([('name', 'penny'), ('phone', '01012345678'), ('birth', '1111')])

## dictionary.clear()  --> key:value 쌍 모두 지우기

# Key로 Value 얻기(get)
print(user.get('name'))  # penny
print(user.get('phone')) # 01012345678

# 딕셔너리 내에 찾으려는 Key 값이 없을 경우 미리 정해 둔 default로 출력 가능
print(user.get('address', 'secret'))   # secret