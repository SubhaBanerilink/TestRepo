

#This program is updted by Shubha Banerjee

class MyPrettyCalculator:
        FirstNum= 0
        SecondNum=0
        Italics=0
        bold= 0
        textSize=0

        def add(self):
            print(type(self).FirstNum + type(self).SecondNum)
        ##def sub(self):
        ##    print(self.FirstNum - self.SecondNum)    
        ##def mul(self):
        ##    print(self.FirstNum * self.SecondNum)
        ##def div(self):
        ##    print(self.FirstNum / self.SecondNum)
        ##def ToThepower(self):
        ##    print(self.FirstNum ** self.SecondNum)


mpc= MyPrettyCalculator()
MyPrettyCalculator.FirstNum=12
MyPrettyCalculator.SecondNum=10
mpc.add()

mpc1= MyPrettyCalculator()
mpc1.add()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Employees:


  def __init__(self, Name, Age, Sex, Salary):
      self.mName=Name
      self.mAge=Age
      self.mSex=Sex
      self.mSalary=Salary
      print("Parameterized Constructor")

  
  def printAttributes(self):
       print(color.BLUE + BFMStart+str(self.mName) +"/"+ str(self.mAge)+"/"+str(self.mSex)+"/"+str(self.mSalary)+BFMStop) 

BFMStart="\033[1m"
BFMStop="\033[0m"
Emp= Employees("Shubha", 12, 'M',123.5);
Emp.printAttributes()



