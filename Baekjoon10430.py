#(A+B)%C == ((A%C) + (B%C))%C  ?
#(A*B)%C == ((A%C)*(B%C))%C  ?

a, b, c = map(int, input().split())
#변수 a, b, c를 한줄로 입력받는다.
# a = int(a)
# b = int(b)
# c = int(c)
#input()은 str이기에 int로 형변환
print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
#각 항목 출력