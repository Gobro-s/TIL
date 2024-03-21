def solution(answers):
    answer = [0, 0, 0]
    supoja1 = [1, 2, 3, 4, 5]
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        ans = answers[i]
        if(supoja1[i % len(supoja1)] == ans):
            answer[0] += 1
        if(supoja2[i % len(supoja2)] == ans):
            answer[1] += 1
        if(supoja3[i % len(supoja3)] == ans):
            answer[2] += 1
            
    result = []
    for j in range(len(answer)):
        if(answer[j] == max(answer)):
            result.append(j+1)
    return sorted(result)