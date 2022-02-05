size = eval(input())
list = []
for i in range(size):
    num = eval(input())
    list.append(num)
list.sort()
for i in list:
    print(i)
