x, y, w, h = map(int, input().split(" "))

list = []
list.append(x)
list.append(y)
list.append(abs(x - w))
list.append(abs(y - h))
print(min(list))
