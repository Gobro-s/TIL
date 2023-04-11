x, y, w, h = map(int, input().split())

rst = []
disx = w-x
disy = h-y
rst.append(disx)
rst.append(disy)
rst.append(x)
rst.append(y)

print(min(rst))