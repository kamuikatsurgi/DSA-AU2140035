num = int(input("Enter a number: "))

def addup(n):
    assert n>0 and n%1==0, "enter a valid number"
    if n==1:
        return 1
    else:
        return n + addup(n-1)

print(addup(num))