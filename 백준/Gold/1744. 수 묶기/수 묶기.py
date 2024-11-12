N = int(input())
nums = [int(input())for _ in range(N)]

list_positive = [i for i in nums if i >= 1]
list_negative = [i for i in nums if i <= 0]
summary = 0

list_positive.sort()
list_positive.reverse()			
list_negative.sort()

for i in range(0,len(list_positive)-1,2):
    if list_positive[i] != 1 and list_positive[i+1] != 1:
        summary += list_positive[i] * list_positive[i+1]
        list_positive[i] = 0
        list_positive[i+1] = 0
summary += sum(list_positive)

for i in range(0,len(list_negative)-1,2):
    summary += list_negative[i] * list_negative[i+1]
    list_negative[i] = 0
    list_negative[i+1] = 0
summary += sum(list_negative)

print(summary)