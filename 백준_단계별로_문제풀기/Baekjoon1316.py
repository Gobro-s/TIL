n = int(input())

group_word = 0  # 그룹 단어인가
for _ in range(n):
    word = input()
    error = 0   # 그룹 단어가 아닌가
    for i in range(len(word)-1):  #  
        if word[i] != word[i+1]:  # 이어진 두 문자가 다르면
            new_word = word[i+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[i]) > 0:  # 남은 문자열에 현재 단어 있으면?
                error += 1  # error +1
    if error == 0:  
        group_word += 1  # error ==0 이어야 그룹 단어 +1
print(group_word)