class Rectangle():
    def __init__(self):
        self.nom = "Rectangle"
        self.longueur = 0 
        self.largeur = 0 
        
    
    def set_form(self):
        if self.nom == "Rectangle":
            longueur = int(input("Inserez la longueur"))
        else :
            longueur = 0
        largeur = int(input("Inserez la largeur"))
        self.largeur = largeur
        self.longueur = longueur
        
        
    def afficher(self):
        str_affichage  =[]
        str_temp = []
        print(f"{self.nom} : Long = {self.longueur} Larg = {self.largeur}")
        self.surface()
        for i in range(self.largeur):
            for j in range(self.longueur):
                str_temp.append("■")
            str_affichage.append(str_temp)
            str_temp = []
        print(str_affichage)    
            
    def surface(self):
        surface = self.longueur*self.largeur
        print(f"Surface = {surface}")
                
        
        

class Carre(Rectangle):
    def __init__(self):
        super().__init__()
        self.nom = "carré"
        
    def set_form(self):
        self.longueur = self.largeur
        return super().set_form()
    
        
    
    
    


def main():
    Forme1 = Rectangle()
    Forme1.set_form()
    Forme1.afficher()
    Forme2 = Carre()
    Forme2.set_form()
    Forme2.afficher()
    



if __name__ =="__main__":
    main()