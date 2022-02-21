import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
numbers = []
# count = [0] * 8001

for _ in range(n):
  i = int(sys.stdin.readline())
  numbers.append(i)
  # count[i] += 1

print(round(sum(numbers) / n))

numbers.sort()
print(numbers[int((n/2) - 0.5)])

count = Counter(numbers).most_common(2)
if n == 1:
  print(count[0][0])
else:
  if count[0][1] != count[1][1]:
    print(count[0][0])
  else:
    print(count[1][0])
# fre = count.index(max(count))
# if fre > 4000:
#   fre -= 8000
# print(fre)

print(max(numbers) - min(numbers))