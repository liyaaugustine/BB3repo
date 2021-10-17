a=input("Enter any word :")
print(a)
r=a[::-1]
print(r)
if a==r:
    print(a,'is palindrome string')
else:
    print(a," is not palindrome")
n=int(input("Enter any number :"))
temp=n
rev=0
while n>0:
    ans=n%10
    rev=rev*10+ans
    n=n//10 #to avoid point value
    print(rev)
if temp==rev:
    print("number is palindrome")
else:
    print("number is not palindrome")