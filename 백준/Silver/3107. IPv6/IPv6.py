li = [-1] * 39
li[4] = li[9] = li[14] = li[19] = li[24] = li[29] = li[34] = ":"
ind = 38
ipv6 = input()
sp = ipv6.split(":")
colonCnt = 0

if len(sp) > 8:
    if sp[-1] == "" and sp[-2] == "":
        sp.pop()
        
for i in range(7, -1, -1):
    if len(sp) <= 7-i:
        now = ""
        
    else:
        now = sp[i-8]
        
    if now == "":
        colonCnt += 1
        
        if colonCnt == 1:
            
            for k in range(8-len(sp)):
                sp.insert(i-8, "")
            colonCnt = -9
    
    for j in range(1, 5):
        
        if j > len(now):
            li[ind] = "0"
        
        else:
            li[ind] = now[-j]
        ind -=1
    ind-=1
num = "".join(li)

print(num)