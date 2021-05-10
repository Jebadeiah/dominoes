# put your python code here
from math import sqrt

gza = int(input())
rza = int(input())
odb = int(input())
wu = (gza + rza + odb) / 2
print(sqrt(wu * (wu - gza) * (wu - rza) * (wu - odb)))
