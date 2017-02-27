class Student(object):

    def __init__(self,name,id,age):
        self.student_name = name
        self.id = id
        self.age = age
    def GetId(self):
        return(self.id)
    def GetName(self):
        return(self.student_name)
    def GetAge(self):
        return(self.age)

class Standard(Student):
    def __init__(self,name,id,age,std):
        Student.__init__(self,name,id,age)
        self.std = std
    def GetClass(self):
        return(self.std)

class House(Standard):
    def __init__(self,name,id,age,std):
        Standard.__init__(self,name,id,age,std)
        self.blue = []
        self.red = []
        self.green = []
        self.yellow = []
        self.allocateHouse(id)
    def allocateHouse(self,idd):
        if (idd % 4) == 0:
            self.YellowHouse(idd)
        elif (idd % 3) == 0:
            self.GreenHouse(idd)
        elif (idd % 2) == 0:
            self.RedHouse(idd)
        else:
            self.BlueHouse(idd)
    def YellowHouse(self,id):
        self.yellow.append(id)
    def GreenHouse(self,id):
        self.green.append(id)
    def RedHouse(self,id):
        self.red.append(id)
    def BlueHouse(self,id):
        self.blue.append(id)
    def GetHouse(self):
        id = self.GetId()
        if id in self.blue:
            return('blue')
        elif id in self.red:
            return('red')
        elif id in self.green:
            return('green')
        elif id in self.yellow:
            return('yellow')
        else:
            return('error')
    def PrintRecord(self):
        print("Name = ",self.GetName(),", Id = ",self.GetId(),", Age = ",self.GetAge(),", Standard = ",self.GetClass(),", House = ",self.GetHouse())

obj1 = [House("ketul",1,6,1),House("rahul",2,6,1)]
for x in range(3):
    obj1.append(House(input("Name="),int(input("Id=")), int(input("Age=")), int(input("Std="))))

for x in range(len(obj1)):
    obj1[x].PrintRecord()