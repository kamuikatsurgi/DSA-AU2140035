s = input("Enter a string to check for palindrome: ")
length =len(s)

def ispali(k,n):
    if n>0:
        return k[n] + ispali(k, n-1)
    else:
        return k[0]

new_s = ispali(s, length-1)

if new_s == s:
    print("the string is a palindrome")
else: 
    print("it is not a palindrome")