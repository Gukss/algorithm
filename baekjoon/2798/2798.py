n, m = map(int, input().split(" "))

numbers = list(map(int, input().split()))
numbers.sort()

count = 0
minus = 0
result = 0

for i in range(0, n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      if (numbers[i] + numbers[j] + numbers[k] <= m):
        result = max(result, numbers[i] + numbers[j] + numbers[k])
      else:
        continue

print(result)
