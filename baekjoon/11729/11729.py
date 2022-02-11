input_num = int(input())
count = 0
list = []
def hanoi(n, fm, to, ast):
  global count
  count += 1
  if(n == 1):
    list.append([str(fm), str(to)])
    return
  hanoi(n-1, fm, ast, to)
  list.append([str(fm), str(to)])
  hanoi(n-1, ast, to, fm)

hanoi(input_num, 1, 3, 2)

print(count)
for i in list:
  print(' '.join(i))