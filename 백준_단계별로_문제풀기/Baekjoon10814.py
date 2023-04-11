tri = list(map(int, input('각 변을 입력하세요 : ').split()))
tri.sort()
a=tri[0]
b=tri[1]
c=tri[2]

if a == b == c:
    print('정삼각형')
elif a+b>c:
    if a**2 + b**2 == c**2:
        print('직각삼각형')
    elif a==b!=c or a!=b==c or b==c!=a:
        print('이등변 삼각형')
    else:
        print('삼각형')
else:
    print('삼각형 아님')