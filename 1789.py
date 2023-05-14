while True:
  try:
    num = int(input())
    if not num:
      break
    lesmas = list(map(int,input().split()))
    if max(lesmas) < 10:
      print(1)
    elif max(lesmas) >=10 and max(lesmas) < 20:
      print(2)
    else:
      print(3)
  except EOFError:
    break
