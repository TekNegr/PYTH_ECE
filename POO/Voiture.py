class Voiture():
    def __init__(self) :
        self.marque = None
        self.model = None
        self.vitesse = 0
        self.moteur = None 
        self.constructor()
        self.Use_car()
        
    def constructor(self):
        print("Vous allez initialiser une voiture :")
        marque = str(input("Quelle est la marque de votre voiture ?"))
        self.marque = marque
        model = str(input("Quelle est le model de votre voiture ?"))
        self.model = model
        moteur_choix = int(input("""Quelle est la moteur de votre voiture ?
                           1-essence
                           X-diesel"""))
        if moteur_choix ==1:
            moteur="Essence"
        else:
            moteur="Diesel"
        self.moteur = moteur
        
    def accélerer(self):
        self.vitesse+=10
    
    def afficher_vitesse(self):
        print(f"Vitesse = {self.vitesse}.km")
        
    def Car_Stats(self):
        print(f"""Marque : {self.marque}
              Modele : {self.model}
              Moteur: {self.moteur}
              """)
        
    def Use_car(self):
        choix = int(input("""Voulez vous entrer dans votre voiture ? 
                          1- Oui
                          0- Non"""))
        while(choix>=1):
            self.afficher_vitesse()
            choix = int(input("Appuyer sur 2 pour accéler 3 pour afficher les stats de votre voiture ou 0 pour quitter"))
            if choix ==2:
                self.accélerer()
                choix = 1
            elif choix ==3:
                self.Car_Stats()
                choix = 1
    

def main():
    voiture_n = Voiture()
    voiture_n.afficherVoiture



if __name__ =="__main__":
    main()