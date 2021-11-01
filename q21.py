import math
x,y = map(int,input().split())

z = math.sqrt(x**2+y**2)

if z>100:
    print("outside\n")

else:
    print("inside\n")
