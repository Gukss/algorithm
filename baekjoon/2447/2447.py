input_num = int(input())

def draw_star(length):
  if length == 1:
    return ['*']
  
  star = draw_star(length//3)
  list = []
  for i in star:
    list.append(i * 3)
  for i in star:
    list.append(i + ' ' * (length//3) + i)
  for i in star:
    list.append(i * 3)
  return list

result = draw_star(input_num)
for i in result:
  print(i)