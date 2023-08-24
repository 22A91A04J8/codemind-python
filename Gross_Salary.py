a=int(input())
b=(0.8*a+a*0.2)+a
c=(0.9*a+0.25*a)+a
d=(0.95*a+0.3*a)+a
if a<=10000:
    print(f"{b:.2f}")
elif a<=20000:
    print(f"{c:.2f}")
else:
    print(f"{d:.2f}")
