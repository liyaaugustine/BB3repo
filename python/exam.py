def pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('*',end=" ")
        print("\r")
n=5
pyramid(n)


#"r = lambda q: q * 2 "
#"s = lambda q: q * 3"
 #x = 2
  #x = r(x) #r(2) 
   #x = s(x)#r(4) here x becomes 4
    #x = r(x)#r(12) here x becomes 12
     #print (x)"
def num(n):
   num=1
    for i in range(0,n):
        num=1
        for j in range(0,i+1):
            print(num,end=" ")
            num=num+1
        print('\r')
n=5
num(n)
