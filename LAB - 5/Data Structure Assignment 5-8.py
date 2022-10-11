a = []
n = int(input("Enter size of array:"))
for i in range(n):
    l = int(input("Enter array element:"))
    c = [l]
    a = a+c
print(a)

def counting_Sort(arr, value):
    n = len(arr)
    output = [0]*(n)
    count = [0]*(10)
    for i in range(0, n):
        k = (arr[i] / value)
        count[int((k) % 10)] += 1

    for i in range(1,10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        k = (arr[i] / value)
        output[count[int((k) % 10) ] - 1] = arr[i]
        count[int((k) % 10)] -= 1

    for i in range(0,len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max_element = max(arr)
    exp = 1
    while max_element/exp > 0:
        counting_Sort(arr,exp)
        exp *= 10
    return arr
print(radixSort(a))
