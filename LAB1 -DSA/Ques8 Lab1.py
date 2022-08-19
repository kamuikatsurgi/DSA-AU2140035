s = input("Enter a string to check for palindrome: ")
length =len(s)

def reverse(k,n):
    if n>0:
        return k[n] + reverse(k, n-1)
    else:
        return k[0]
reverse_s = reverse(s,length-1)
print("The reverse of the given string is:  ",reverse_s)