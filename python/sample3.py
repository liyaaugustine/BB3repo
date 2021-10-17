class myclass:
    year=2020 #it is an class variable (others are object variable)

    def __init__(self,name,age): #init fn run each time when an object create.
        self.myname=name
        self.myage=age
        print('Good mng ' + self.myname)
    def newhalo(self,place):
        self.myplace=place
        print(self.myage)
    def halo(self):
        print('Halo '+self.myplace)
    def addage(self):
        self.newage=self.myage+1
        print('new age of rose is ',self.newage) #because it is only calling in employe object. so (rose)
    @classmethod  #standerd way
    def addyr(cls):
        cls.yr=cls.year+1
        print(cls.yr)
student=myclass('milna',42)
student.newhalo('calicut')
student.halo()
employe=myclass('rose',12)
employe.newhalo('dubai')
employe.halo()
employe.addage()
employe.addyr()
class vehicle:
    def __init__(self):
        print('parent class init')
    def veh(self):
        print('This is parent class')
class bike(vehicle):
    def __init__(self):
        super().__init__()  #super means parent class.child class $ parent class init will print if we use super.
        print("child class init")
    def bk(self):
        print('This is child class')
mybike=bike()     
mybike.veh()
mybike.bk()   
