import random
a = []
n = int(input("Enter size of array:"))
for i in range(n):
    l = int(input("Enter array element:"))
    c = [l]
    a = a+c
print(a)

def partition(a, left, right):
    pivot = a[left]
    i = left + 1
    for j in range(left + 1, right):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[left], a[i - 1] = a[i - 1], a[left]
    return i - 1

def quick_sort_random(a, left, right):
    if left < right:
        pivot = random.randint(left, right - 1)
        a[pivot], a[left] = a[left], a[pivot]
        pivot_index = partition(a, left, right)
        quick_sort_random(a, left, pivot_index)
        quick_sort_random(a, pivot_index + 1, right)
    return a

print(quick_sort_random(a,0,len(a)))