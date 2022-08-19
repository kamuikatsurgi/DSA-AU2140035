num = int(input("Enter a factorial number: "))

def fac(n):
    assert n>0 and n%1==0, "enter a valid number"
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(num))