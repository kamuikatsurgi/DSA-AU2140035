x=float(input("Enter number1:"))
y=float(input("Enter number2:"))
a=int(x)
b=int(y)
def hcf(x,y):
    if(x<=y):
        if(y%x==0):
            print(x)
        else:
            t=y%x
            hcf(t,x)
    else:
        if(x%y==0):
            print(y)
        else:
            t=x%y
            hcf(t,y)

if(x==a and b==y):
    c=hcf(a,b)
else:
    print("We can not obtain GCD")