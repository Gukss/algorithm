input_num = input().split(" ")
list = []

for i in input_num:
  list.append(int(i))

list.sort()
set_list = set(list)

if len(set_list) == 1:
  print(10000 + list[0] * 1000)
elif len(set_list) == 3:
  print(list[-1] * 100)
else:
  print(1000 + list[1] * 100)