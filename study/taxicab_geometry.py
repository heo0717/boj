import math

R = int(input())

euclidean_geometry = ( R**2 ) * math.pi
taxicab_geometry = ( (2 * R) ** 2 ) / 2

print('%.6f'%euclidean_geometry)
print('%.6f'%taxicab_geometry)