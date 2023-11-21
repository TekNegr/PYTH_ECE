class MaClasse:
    
    x = 28
    y = x+5
        
    def affiche(self):
        self.z = 42
        print(f"y = {self.y} ; z={self.z}")
        

def main():
    print("ceci est le main")
    Objet = MaClasse()
    Objet.affiche()


if __name__ == "__main__":
    main()