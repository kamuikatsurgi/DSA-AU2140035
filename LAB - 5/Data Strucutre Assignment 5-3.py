a = []
n = int(input("Enter size of array:"))
for i in range(n):
    l = int(input("Enter array element:"))
    c = [l]
    a = a+c
print(a)


def binarySearch(c, a):
    d = 0
    e = len(c) - 1
    while d <= e:
        mid = (d+e) // 2
        if a <= c[mid] : 
            e = mid - 1
        else :
            d = mid + 1
    return d

def insertionsort(a):
    b=len(a)
    c=[]
    c=c+[a[0]]
    count=1
    for i in range(count,b):
        d=binarySearch(c,a[i])
        count=count+1
        c.insert(d,a[i])
    return c

print(insertionsort(a))
    















