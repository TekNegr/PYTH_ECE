class CompteBancaire():
    def __init__(self, somme_tot, nr_compte, Nom_User):
        self.nr_compte = nr_compte
        self.nom = Nom_User
        self.balance = somme_tot
        
    
    def depot(self, somme):
        self.balance += somme
        
    def retrait(self, somme):
        self.balance -= somme
    
    def afficher(self):
        print(f"""AFFICHAGE DU COMPTE
              BONJOUR {self.nom}!! 
              #Compte : {self.nr_compte}
              balance : {self.balance}
              """)
        
    def Interact(self):
        choix = int(input("""Que voulez vous faire ? 
                      1- Changer l'user
                      2- Faire un dépot 
                      3- Faire un retrait 
                      Autre- Quitter"""))
        
        if choix ==1:
            Nom = input("Qui est le nouveau user ?")
            self.nom = Nom
            choix = 0
            
        elif choix==2:
            Somme = int(input("Combien voulez vous deposer?"))
            self.depot(Somme)
            choix = 0
        
        elif choix==3:
            Somme = int(input("Combien voulez vous retirer?"))
            self.retrait(Somme)
            choix = 0
            
        else:
            print(f"Aurevoir {self.nom}")
            return 0
        
        
def CreateAccount():
    print("Initialiser votre compte bancaire:")
    Nom = input("Nom :")
    Nr_Compte = input("Num Compte :")
    Balance = int(input("Balance :"))
    Compte = CompteBancaire(Balance, Nr_Compte, Nom )
    return Compte
    
def main():
    Db_Compte = []
    Nb_compte = int(input("Combien de compte voulez vous créer"))
    usage = 0
    for i in range(Nb_compte):
        Compte_temp = CreateAccount()
        Db_Compte.append(Compte_temp)
        Compte_temp = None
    
    for i in range(len(Db_Compte)):
        print(f"{i}: {Db_Compte[i].nom}")
    Choix = int(input("Choisissez votre compte (Rien inserer si quitter)"))
    Db_Compte[Choix].afficher()
    Db_Compte[Choix].Interact()
            
                
        
if __name__ == "__main__":
    main()