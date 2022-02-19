n = int(input())
result = 0

for i in range(1000000):
  if i > n:
    continue

  count = i
  str_num = str(i)
  num_len = len(str_num)

  for j in range(num_len):
    count += int(str_num[j])

  if count == n:
    result = i
    break
print(result)

