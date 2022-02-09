# 백준 1193번

## 분수찾기

---

```python
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
```

```python
# 1  2   6   7  15  16
# 3  5   8  14  17
# 4  9  13  18
#10 12  19
#11 20
#21
```

> 위 순서로 진행된다.  
> 1, 2, 6, 7, 15를 기준으로 왼쪽 대각선 아래 방향으로 줄을 센다.  
> ex ) 19는 6 번째 줄이다.

> 줄을 저장하는 line 변수와 그 줄에서 가장 큰 수를 저장하는 max_num을 선언한다.

> line은 +1, max_num은 +line을 하면서 max_num이 input_num보다 커질 때 까지 반복문을 반복한다.  
> max_num이 input_num보다 커지면 input_num이 해당 line에 위치한다는 의미이다.

> max_num과 input_num의 차이를 구한다.

> line이 홀수일 때, 짝수일 때 구분한다.  
> top이 분자, bottom이 분모이다.

> 짝수일 때: 분모는 1 + diff, 분자는 line - diff의 규칙을 가진다.
