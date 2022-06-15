class Schoolar:
    
    def intializer(self,name,score):
        self.name = name
        self.score= score
    
    def showData(self):
        print("Name:",self.name)
        print("Score:",self.score)
    
    def isAproved(self):
        if self.score >= 6: 
            print(self.name,": Approved") 
        else: 
            print(self.name,": Reproved")

studen1 = Schoolar()
studen2 = Schoolar()

studen1.intializer("Roberto",9)
studen2.intializer("Juan",5)
studen1.showData()
studen2.showData()
studen1.isAproved()
studen2.isAproved()