num=int(input("Enter Number :"))
flag=True
if num==1:
    print('Number is not prime ')
elif num<1:
    print('Enter posive number')
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")