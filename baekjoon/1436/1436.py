n = int(input())
num_count = 0

for i in range(1000000000):
  str_num = str(i)
  count6 = 0
  for j in range(len(str_num) - 1, -1, -1):
    if str_num[j] == '6':
      count6 += 1
    if count6 == 3:
      num_count += 1
      break
    if str_num[j-1] != '6':
      count6 = 0
  if num_count == n:
    print(i)
    break
