length = int(input("enter length of an array: "))
n = []
for i in range(length):
    input_n = int(input("enter element: "))
    n.append(input_n)
print(n)

def prodarray(list, num):
    assert num>=0, "assertion error"
    if num==0: 
        return list[0]
    else:
        return list[num]*prodarray(list, num-1)

print(prodarray(n,length-1))


