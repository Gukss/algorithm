import math

a, b, v = input().split()
a = int(a)
b = int(b)
v = int(v)

day = 1

diff = a - b
start = v - a
day += math.ceil(start/diff)
print(day)