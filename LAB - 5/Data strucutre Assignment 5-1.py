a=[]
n=int(input("Enter size of array:"))
for i in range(n):
    l=int(input("Enter array element:"))
    c=[l]
    a=a+c
print(a)

def bubblesort(a):
    b=len(a)
    for i in range(1,b-1):
        count=0
        for j in range(b-i):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                count=count+1
            print(a)
        if(count==0):
            print("Array is already sorted")
            break

bubblesort(a)