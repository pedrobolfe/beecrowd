H, E, A, O, W, X = map(int,input().split())

bem = H + E + A
mal = O + W

if bem>mal:
    print('Middle-earth is safe.')
if bem<=mal:
    bem2 = bem + X
    if bem2>mal:
      print('Middle-earth is safe.')
    else:
        print('Sauron has returned.')