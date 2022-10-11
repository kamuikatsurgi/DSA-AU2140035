a = []
n = int(input("Enter size of array:"))
for i in range(n):
    l = int(input("Enter array element:"))
    c = [l]
    a = a+c
print(a)

def merge_SubSeq(arr, left, right, end, temp):
    a = left
    b = right
    m = 0
    while a < right and b < end:
        if arr[a] < arr[b] :
            temp[m] = arr[a]
            a += 1
        else :
            temp[m] = arr[b]
            b += 1
        m += 1
    while a < right :
        temp[m] = arr[a]
        a += 1
        m += 1
    while b < end:
        temp[m] = arr[b]
        b += 1
        m += 1

    for i in range(end - left):
        arr[i + left] = temp[i]

def Merge_recSort(arr, first, last, temp):
    if first == last:
        return
    else :
        mid = (first + last) // 2
    Merge_recSort(arr, first, mid, temp)
    Merge_recSort(arr, mid+1, last, temp)
    merge_SubSeq(arr, first, mid+1, last+1, temp)

def merge_Sort(array): 
    n = len(array)
    temp = [-1] * n
    Merge_recSort(array, 0, n-1, temp)
    return temp

print(merge_Sort(a))