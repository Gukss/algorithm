inputNum = input()
num = int(inputNum)
count = 0


def han(num):
  global count
  if(num < 100):
    count += 1
    return
  list = str(num)
  for i in range(len(list)-2):
    diff1=int(list[i]) - int(list[i+1])
    diff2=int(list[i+1]) - int(list[i+2])
    if(diff1 != diff2):
      return
  count += 1
  return

for i in range(1, num+1):
  han(i)
  
print(count)