def solution(my_string):
    answer = ''
    jungbok = []
    for i in my_string:
        if i not in jungbok:
            answer += i
            jungbok.append(i)
            
    return answer