# 백준 2869번

## 달팽이는 올라가고 싶다

---

```python
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
```

> 시간제한이 있는 문제다. 반복문을 사용하면 시간이 오래 걸리기 때문에 반복문을 사용하지 않고 해결하는 문제다.

> 낮에 올라가는 거리 a, 밤에 내려오는 거리 b 의 차이를 diff  
> 마지막 날 낮에 올라가는 a를 막대 높이인 v에서 뺀 start  
> 마지막 날 올라가는 거리를 미리 계산했으므로 day는 1부터 시작한다.

> start를 diff로 나누고 올림해 준 값을 day에 더해주면 된다.

> ex ) 3 1 6 이면  
> diff: 2,  
> start: 3,  
> start/diff: 1.5 -> 올림: 2  
> 최종 day: 3
