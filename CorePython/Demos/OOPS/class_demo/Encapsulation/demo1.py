#class creating 

class emp :
    def __init__(self , id  , name , sal):
        self.id = id 
        self.name = name
        self.sal = sal 

    def getId(self):
        return self.id
    def setId(self , id):
        self.id = id 
    def display(self):
        print(f"ID ={self.id} \n name ={self.name} \n sal ={self.sal}")
el = emp(101 , "Hanmant" , 123456)
el.display()