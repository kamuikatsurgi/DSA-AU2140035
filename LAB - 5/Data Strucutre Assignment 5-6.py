a = []
n = int(input("Enter size of array:"))
for i in range(n):
    l = int(input("Enter array element:"))
    c = [l]
    a = a+c
print(a)

def swap(a, i, j):
        temp = None
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

def quick_sort(a, l, h):
    left = l
    right = h
    pivot = a[(l + h) //2]
    if l>= h:
        return
    while left <= right:
        while a[left] < pivot:
            left += 1
        while a[right] > pivot:
            right -= 1
        if left <= right:
            swap(a, left, right)
            left += 1
            right -= 1
    quick_sort(a, l, right)
    quick_sort(a, left, h)
    return a

print(quick_sort(a,0,len(a)-1))