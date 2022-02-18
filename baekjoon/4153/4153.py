while True:
  numbers = list(map(int, input().split(" ")))
  max_num = max(numbers)
  if sum(numbers) == 0:
    break
  numbers.remove(max_num)
  if (max_num ** 2) == (numbers[0] ** 2) + (numbers[1] ** 2):
    print('right')
  else:
    print('wrong')
