a=[]
n=int(input("Enter size of array:"))
for i in range(n):
    l=int(input("Enter array element:"))
    c=[l]
    a=a+c
print(a)

def selectionsort(a):
    b=len(a)
    for i in range(b-1):
        min=i
        for j in range(i,b):
            if(a[min]>a[j]):
                temp=a[min]
                a[min]=a[j]
                a[j]=temp
        print(a)

selectionsort(a)
            
            