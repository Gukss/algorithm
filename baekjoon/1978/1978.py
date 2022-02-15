import math

n = int(input())
count = 0
numbers = list(map(int, input().split()))

for num in numbers:
  prime = 1
  if num == 1:
    prime = 0
  for i in range(2, num):
    if(num % i == 0):
      prime=0
      break
  if prime == 1:
    count += 1
print(count)