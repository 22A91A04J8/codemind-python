a,b,c,d,e=map(int,input().split())
s=(a+b+c+d+e)/5
if s>=90:
    print("Grade A")
elif s>=80 and s<=90:
    print("Grade B")
elif s<=80 and s>=70:
    print("Grade C")
elif s<=70 and s>=60:
    print("Grade D")
elif s<=60 and s>=40:
    print("Grade E")
else:
    print("Grade F")
