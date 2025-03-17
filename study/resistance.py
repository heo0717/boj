import sys
input = sys.stdin.readline

color = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4,
         'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

first = input().strip()
second = input().strip()
third = input().strip()

# ( f + s ) * t
f = color.get(first)
s = color.get(second)
t = color.get(third)

a = str(f) + str(s)
print(int(a) * (10 ** t))