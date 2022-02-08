# 1 - 1개
# 2~7 - 2개 -- 1, 6
# 8~19 - 3개 -- 6, 12
# 20~37 - 4개 -- 12, 18

# 1개
# 6개
# 12개
# 18개

num = int(input())

def check(num):
  if(num ==1):
    print(1)
    return
  num = num-2
  count = 1
  while(num >= 0):
    num = num - (count * 6)
    count += 1
  print(count)

check(num)