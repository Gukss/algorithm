list1 = []
for i in range(10000):
    list1.append(i+1)

list2 = []


def selfNum(list1, list2, n):
    num = n
    for i in range(len(str(n))):
        num += (n % 10)
        n = int(n / 10)
    if(num > 10000):
        return
    list2.append(num)
    return


for i in range(10000):
    selfNum(list1, list2, i+1)

a = [x for x in list1 if x not in list2]
for i in a:
    print(i)
