# https://www.acmicpc.net/problem/5622

word = input()
sms = {1 : '', 2 : 'ABC', 3:'DEF', 4:'GHI', 5:'JKL',
        6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ', 0:''}

time = 0

for i in word:
    for key, value in sms.items():
        if i in value:
            time += key +1

print(time)