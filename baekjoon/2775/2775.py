result = []

def check():
  global result
  t = int(input())
  
  for num in range(t):
    k = int(input())
    n = int(input())
    
    count = 0  
    list=[]
    newList = []
    for i in range(n):
      list.append(i+1)
    
    for i in range(k):
      for j in range(n):
        count+=list[j]
        newList.append(count)
      list = newList.copy()
      newList.clear()
      count = 0
    
    result.append(list[n - 1])

check()
for i in result:
  print(i)