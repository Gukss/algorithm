# 백준 1929번

## 소수 구하기

---

```python
m, n = map(int, input().split(" "))
```

> 입력값 받기

```python
for i in range(m, n+1):
  if i == 1:
    continue
  prime = 1
```

> m 부터 n까지 반복문을 반복한다.  
> i가 1일 때 continue한다.  
> 소수를 판별할 prime 변수를 1로 초기화 한다.

```python
	for num in range(2, int(i**0.5) + 1):
    if i % num == 0:
      prime = 0
      break
  if prime == 1:
    print(i)
```

> 위 for 문 안에서 진행된다.  
> 해당 for문은 2 부터 i의 제곱근 까지 반복한다.  
> 바깥 반복의 i가 안쪽의 반복의 num으로 나누어 지면 prime = 0을 하고 반복문을 탈출하고 아래의 if문으로 간다.  
> prime이 1이면 i를 출력한다.

```python
m, n = map(int, input().split(" "))

for i in range(m, n+1):
  if i == 1:
    continue
  prime = 1
  for num in range(2, int(i**0.5) + 1):
    if i % num == 0:
      prime = 0
      break
  if prime == 1:
    print(i)
```
