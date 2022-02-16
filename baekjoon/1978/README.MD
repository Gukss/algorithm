# 백준 1978번

## 소수 구하기

---

```python
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
```

> 1929 번과 같이 제곱근 까지만 구해도 가능하다.  
> range(2, int(i\*\*0.5)+1)를 활용한다.
