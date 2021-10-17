x=int(input('Enter Number :'))
temp=x
sum=0
while temp!=0:
    rem=temp%10
    sum=sum+rem*rem*rem
    temp=int(temp/10)
if sum==x:
    print("Number is armstrong")
else:
    print("Number is not armstrong")