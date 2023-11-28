import datetime
from typing import Any 
from functools import total_ordering


class Person():
    def __init__(self, nom, prenom, DdN, Statut):
        self.nom = nom
        self.prenom = prenom
        self.Statut = Statut
        self.CreateBirthday(DdN)
        
    def CreateBirthday(self, DdN):
        
        if len(DdN) != 3 or not all(isinstance(val, int) for val in DdN):
            print("Invalid input. Please provide a list of three integers for year, month, and day.")
            return
        
        try:
            Birthday = datetime.date(DdN[0], DdN[1], DdN[2])
        except ValueError as e:
            print(f"Error creating birthday: {e}")
            return    
            
        Now = datetime.date.today()

        age = Now.year - Birthday.year 
        if Now.month < Birthday.month or (Now.month == Birthday.month and Now.day < Birthday.day):
            age -=1
            
        if Birthday == Now:
            print("Happy Birthday to you")
        self.birthday = Birthday
        self.age = age       
        

    def Handle(self):
        pass
    
    def print(self):
        print(f"""
              Carte d'Identité {self.Statut}
              Nom : {self.nom} 
              Prenom: {self.prenom}
              Date De Naissance : {self.birthday} | {self.age} ans
              """)
        
class Produit():
    def __init__(self, Prod_Name, Prix : int, Nb_Prod =1):
        self.Nom = Prod_Name
        self.Prix = Prix
        self.Nb_Prod = Nb_Prod
    
    def print(self):
        print(f"{self.Nom} :{self.Prix}x{self.Nb_Prod}({self.Prix * self.Nb_Prod}€) ")

class Customer(Person):
    def __init__(self, nom, prenom, DdN, Statut="Customer"):
        super().__init__(nom, prenom, DdN, Statut)
        self.Cart = []
        self.Solde = 0
        
    def AddToCart(self, Prod: Produit):
        if Prod is not None:
            if Prod not in self.Cart:
                self.Cart.append(Prod)
            else :
                self.Cart[Prod].Nb_Prod +=1
            self.UpdateCart()
                
    def UpdateCart(self):
        solde = 0
        for prod in self.Cart:
            solde += prod.Prix * prod.Nb_Prod
        self.Solde = solde
            
    def print(self):
        super().print()
        for prod in self.Cart:
            print(f"{prod}\n")
        print(f"Total = {self.Solde}")
        
        
class Employe(Person):
    def __init__(self, nom, prenom, DdN, Statut="Employé"):
        super().__init__(nom, prenom, DdN, Statut)
        self.Job_Pos = ["Employé", "Technicien", "Manager", "Cadre"]
        
    #fonction pour pouvoir faire les comparaisons entre les positions   
    #>=
    def __ge__(self,Otr_Pos):
        if not isinstance(Otr_Pos,str):
            raise ValueError("EUh... Job Please!")
        
        if Otr_Pos not in self.Job_Pos:
            raise ValueError(f"'{Otr_Pos}' n'est pas un job dans mon monda ca...")
        
        self_index = self.Job_Pos.index(self.Statut)
        otr_index = self.Job_Pos.index(Otr_Pos)
        return self.Statut >= Otr_Pos
    
    #==
    def __eq__(self,Otr_Pos):
        if not isinstance(Otr_Pos,str):
            raise ValueError("EUh... Job Please!")
        
        if Otr_Pos not in self.Job_Pos:
            raise ValueError(f"'{Otr_Pos}' n'est pas un job dans mon monda ca...")
        
        self_index = self.Job_Pos.index(self.Statut)
        otr_index = self.Job_Pos.index(Otr_Pos)
        return self.Statut == Otr_Pos
    
    def Handle(self):
        super().Handle()
        pos = str(input("Choisissez votre promotion :"))
        self.AddPromotion(pos)
        
    def AddPromotion(self, Position):
        if Position in self.Job_Pos:
            self.Statut = Position
        
    def print(self):
        super().print()
        
        
class PersonHandler():
    def Create_Person(self):
        Nom = str(input("Quel est votre nom?"))
        Prenom = str(input("Quel est votre prenom?"))
        Db = int(input("Entrez votre jour de Naissance"))
        Mb = int(input("Entrez votre Mois de Naissance"))
        Yb = int(input("Entrez votre année de Naissance"))
        DdN = [Yb,Mb,Db]
        Statut=str(input("""
                         Quel est votre statut à nos yeux ?
                         Customer / Employe 
                         (écrire en toute lettre)"""))
        if Statut == "Customer":
            person1 = Customer(Nom, Prenom, DdN)
        elif Statut == "Employe":
            person1 = Employe(Nom, Prenom, DdN)
            
        