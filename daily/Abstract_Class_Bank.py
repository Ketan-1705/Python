from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(self,r):
        pass
class HDFC(RBI):
        
    def display(self):
        print("This is HDFC")
    def roi(self,r):
        print("rate of interest In HDFC : ",r)
class BOI(RBI):
    def display(self):
        print("This is BOI")
    def roi(self,r):
        print("rate of interest In BOI : ",r)

b1=HDFC()
b1.display()
b1.roi(6.5)

c1=BOI()
c1.display()
c1.roi(7.5)
