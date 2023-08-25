import math
a,b,c=map(int,input().split())
d=float(a+b+c)/2
e=(d)*(d-a)*(d-b)*(d-c)
area=math.sqrt(e)
print(f"{area:.2f}")