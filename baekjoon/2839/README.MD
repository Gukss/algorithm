# 백준 2839번

## 설탕 배달

---

```python
input_num = int(input())
count = 0
```

> 사용할 변수 선언한다. 입력받은 숫자 input_num, 봉지 개수 count

---

```python
while(input_num >= 0):
  if((input_num % 5) == 0):
    count = count + (input_num // 5)
    print(count)
    break
  input_num -= 3
  count += 1
else:
  print(-1)
```

> while, else문을 사용한다.  
> 입력한 숫자가 0보다 클동안 while문을 반복한다.  
> if문을 사용해 입력한 숫자가 5로 나누어 떨어지면 5로 나눈 몫을 count에 더하고 출력하고 반복문을 종료한다.  
> 입력한 숫자가 5로 나누어 떨어지지 않을 때 input_num에서 3을 빼고 count는 1을 더해준다.  
> 반복문을 반복하다 input_num이 0보다 작아져서 반복을 종료하게 된다면 나누어 떨어지지 않는 경우이므로 -1을 출력한다.
