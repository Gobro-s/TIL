a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lst = [a, b, c, d, e]
lst.sort()
avr = round((a+b+c+d+e) / len(lst))
center = lst[len(lst)//2]
print(avr, center, sep='\n')