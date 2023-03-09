seg = int(input())

min = seg//60
seg -= min*60
hr = min//60
min -= hr*60
print(f'{hr}:{min}:{seg}')    