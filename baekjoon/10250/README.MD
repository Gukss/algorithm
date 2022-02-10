# 백준 10250번

## ACM 호텔

---

```python
import math

t = int(input())
list = []
```

> 올림 함수 `math.ceil`를 사용하기 위한 import, t개 입력 데이터, 최종 출력값을 저장하기 위한 list 선언

---

```python
for i in range(t):
  h, w, n = map(int, input().split())
  y = int(n % h)
  x = math.ceil(n / h)
```

> t번 반복  
> input().split()으로 공백을 기준으로 입력값을 나눈 리스트 생성한다.  
> 생성된 리스트를 int()함수를 적용해 반복해 h, w, n에 각각 대입한다.  
> y는 방 번호에서 층 수를 나타낸다.  
> n을 h로 나눈 나머지가 y가 되는 규칙이 있다.  
> x는 방 번호에서 엘리베이터에서 부터 세었을 때의 번호를 나타낸다.  
> x는 n을 h로 나눈 몫을 올림하면 구할 수 있다.

---

```python
	if x < 10:
		x = '0' + str(x)
	else:
		x = str(x)
```

> 아직 위의 for문 안이다.  
> x가 10보다 작으면 yxx, yyxx 형식인 방 번호대신 yx, yyx 형식으로 방 번호가 출력되게 된다. if문에서 x가 10보다 작을때 x앞에 0을 붙여 방 번호의 형식을 yxx, yyxx로 바꿔준다.  
> x의 형식을 문자열로 바꿔준다.

---

```python
	if y == 0:
		y = h
	y = str(y)
	result = y+x
	list.append(result)
```

> 아직 위의 for문 안이다.  
> y가 0이면 제일 위 층이다. y를 0대신 h로 수정해 준다.  
> y의 형식도 문자열로 바꿔준다.  
> result 변수에 문자열 x와 y를 합쳐서 저장한다.  
> list에 result를 추가한다.

> for문 완료

---

```python
for i in range(t):
  print(list[i])
```

> 다른 for문에서 list를 모두 출력한다.

---

### 전체 코드

```python
import math

t = int(input())
list = []

for i in range(t):
  h, w, n = map(int, input().split())
  y = int(n % h)
  x = math.ceil(n / h)
  if x < 10:
    x = '0' + str(x)
  else:
    x = str(x)
  if y == 0:
    y = h
  y = str(y)
  result = y+x
  list.append(result)

for i in range(t):
  print(list[i])
```
