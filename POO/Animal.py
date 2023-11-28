class Animal():
    def __init__(self, age:int , nom:str):
        self.age = age
        self.nommer(nom)
    
    def nommer(self, nom):
        self.nom = nom
        
    def vieillir(self):
        self.age +=1
        
class Reptile(Animal):
    def __init__(self, age, nom):
        super().__init__(age, nom)
        self.nb_ecaille = 1000
        
        
