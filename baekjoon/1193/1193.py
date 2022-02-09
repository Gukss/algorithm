# 1  2   6   7  15  16
# 3  5   8  14  17
# 4  9  13  18
#10 12  19
#11 20
#21

input_num = int(input())
line = 0
max_num = 0

while(max_num < input_num):
  line += 1
  max_num += line

diff = max_num - input_num

if(line % 2 == 0):
  top = line - diff
  bottom = 1 + diff
elif(line % 2 != 0):
  top = 1 + diff
  bottom = line - diff
	
print(str(top) + '/' + str(bottom))