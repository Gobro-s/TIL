# 불 자료형 : 참(True) / 거짓(False) 판별 자료형.
# 참과 거짓 두개의 값만 가능하다.
a = True
b = False
print(type(a), type(b))
# class 'bool', class'bool'

print(1==1)   # True
print(2>1)    # True
print(2<1)    # False

a = [1, 2, 3, 4]
while a:
    print(a.pop())
    # 4
    # 3
    # 2
    # 1

if []: # 만약 []가 참이면
    print('참')
else:
    print('거짓')
# 거짓

if [1, 2, 3, 4]:
    print('참')
else:
    print('거짓')   # 참

print(bool('python'))  # True
print(bool(''))  # False
print(bool({}))  # False
print(bool(()))  # False
print(bool([1, 2, 3]))  # True
print(bool([]))  # False
print(bool(0))  # False
print(bool(5))  # True