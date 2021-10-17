x=10
print(x)
print(type(x))
x='home'
print(type(x))
z=10
y=5
s=z+y
print(s)
a='place'
t='halo'
print(a+t)
mylist=[1,4,5,8,6,3,['yes','no',5.6]]
print(type(mylist))
print(mylist)
print(mylist[6][1])
print(mylist[2:5])
mylist[3:5]=[7,9]
print(mylist)
del mylist[4]
print(mylist)
mylist.insert(0,23)
print(mylist)
mytuple=(1,8,4.2,'halo','happy',(52,56,'name'))
print(mytuple)
print(type(mytuple))
print(mytuple[5])
print(mytuple.count(4.2))
del mytuple
a="""Triple quotes
are using in this"""
print(a[0:5])
a='new string '
print(a)
for m in mylist:
    print(m)
    
print("python is \"object oriented \" language")
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=a+b
print(c)
name=input("Enter your first name:")
last=input("Enter your last name:")
print("Hellow" + " "+ name +last)
studid=2
studname='ram'
print("hellow my name is %s and my id is %d" %(studname,studid))
