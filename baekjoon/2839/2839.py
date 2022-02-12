input_num = int(input())
count = 0

while(input_num >= 0):
  if((input_num % 5) == 0):
    count = count + (input_num // 5)
    print(count)
    break
  input_num -= 3
  count += 1
else:
  print(-1)