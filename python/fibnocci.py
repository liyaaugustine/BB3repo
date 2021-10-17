#def fibnocci(lmt):
lmt=int(input('Enter limit :'))
a=0
b=1
sum=0
count=1
print("Fibnocci Series :")
while count<=lmt:
        print(sum)
        count+=1
        a=b
        b=sum
        sum=a+b


