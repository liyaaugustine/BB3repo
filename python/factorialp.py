num=int(input("Enter Number:"))
ans=1
for i in range(1, num+1):
  ans=ans*i 
  print(ans*i) 
print("Factorial of ",num, "is:", ans)  
if num<0:
    print('Enter any positive number')
