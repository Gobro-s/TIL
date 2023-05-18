# 1. 홍길동씨는 과목별로 국어 80점, 영어 75점, 수학 55점이다. 평균은?

# 1. 딕셔너리로 풀기
score = {'국어' : 80, '영어': 75, '수학': 55}
print(sum(score.values()) / len(score.keys()))

# 2. 리스트로 풀기
subject = ['국어', '영어', '수학']
scores = [80, 75, 55]
print(sum(scores)/len(subject))

# 3. 변수로 풀기
국어 = 80
영어 = 75
수학 = 55
print((국어+영어+수학)/3)


# 75.0


# 2. 자연수 13이 홀수인지 짝수인지 판별하기

if 13 % 2:
    print('홀수')
else:
    print('짝수')

    # 홀수



# 3. 홍길동의 주민번호는 881120-1068234, 주민번호를 앞자리 뒷자리로 나눠 출력해보자

# pin = "881120-1068234"
# yyyymmdd = 
# num = 
# print(yyyymmdd)
# print(num)

pin = "881120-1068234"
print(pin[:6])
print(pin[7:])


# 4. 그럼 홍길동씨의 성별을 나타내는 숫자만 출력하자

print(pin[7:8])
print(pin[7])
