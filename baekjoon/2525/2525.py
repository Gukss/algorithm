a, b = map(int, input().split(" "))
c = int(input())

h = c // 60
m = c % 60

b += m
a += h

if b >= 60:
  a += 1
  b -= 60
if a >= 24:
  a -= 24

print(str(a) + ' ' + str(b))