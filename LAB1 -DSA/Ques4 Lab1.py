num = int(input("enter a number: "))

def fib(n):
    assert n>=0 and n%1==0, "enter a valid number"
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(num))