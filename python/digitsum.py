sum=18
mydict={"name":"ram","age":15,"class":10,"weight":40,"place":"goa"}
print(type(mydict))
print(mydict["class"])
def new(name):
    '''greeting'''
    print("halo"+name)
    return 'changed' + name
z=new('kiran')
print(z)
print(new.__doc__)
def first():
    global x
    x=10
    print(x)
    print(sum)
first()
print("outside",sum)
print(x)
num=int(input("Enter Number:"))
if num>0:
    print("Number is Positive")
    if num==1:
        print("Number is one")
else:
    print("Number is Negative")
newtuple=(1,5,8)
for key,value in mydict.items():
    print(key,'->',value)
print(range(10))
print(list(range(10)))
for item in range(2,50,3):
    print(item)
myarr=[4,5,9]
for index in range(len(myarr)):
    print("Numbers" , myarr[index])
for val in "morning":
    if val=="n":
        continue
    print(val)
def sample():
    pass
sample()
