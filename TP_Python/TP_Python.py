
    
def CodeCarte():
    Correct_dig = 0
    Correct_Code = False
    Code = [6,8,7,5]
    Guess_Code = []
    while Correct_Code == False:
        
        print("inserez votre code secret")
        Guess_Code=[int(input("#"))for _ in range(4)]
        for j in range(len(Code)):
            if Guess_Code[j]==Code[j]:
                Correct_dig +=1
                
        if Correct_dig==4:
            print("Bienvenu User")
            Correct_Code = True
        else : 
            Guess_Code = []
            Correct_dig = 0
            print("Code incorrect Veuillez réessayer")
            
def SommesNum():
    Somme = 0
    Numa = 0
    Choix_Val = False
    while Choix_Val==False:
        Choix_Somme = int(input("""Quelle somme voulez vous faire ?
                                1- Rectangle
                                2-Triangle"""))
        
        if Choix_Somme == 1:
            chx = "Rect"
            Numa=int(input("Jusqu'à où voulez vous faire la somme rectangulaire"))
            Somme = SumRect(Numa)
            Choix_Val = True
        
        elif Choix_Somme == 2:
            chx = "Tri"
            Numa=int(input("Jusqu'à où voulez vous faire la somme triangulaire"))
            Somme = SumTri(Numa)
            Choix_Val = True
        
        else:
            print("Choix invalide, reboot...")  

    print(f"Votre somme {chx}angulaire jusqu'à {Numa} est: {Somme}")
            
def SumRect(Nombre):
    inter_som = 0
    for i in range(Nombre+1):
        for j in range(Nombre+1):
            inter_som += i*j
    return inter_som

def SumTri(Nombre):
    inter_som = 0
    for i in range(Nombre+1):
        for j in range(Nombre+1):
            inter_som += (i+j)
    return inter_som
            
            
def Exo_Expo():
    x = int(input("Choisissez un X"))
    n = int(input("Choisissez un maximum n"))
    approx = Approx_Expo(x,n)
    print(f"Votre approximation est :{approx} ")
    
def Approx_Expo(x, n):
    inter_som = 1
    inter_ex = 1
    for i in range(n):
        i +=1
        inter_som+=(x**i)/inter_ex
        inter_ex *=i
        print(f"Log : {x},{n}, ({x}**{i} / {inter_ex})")
    return inter_som
    
        
    
    
dict_Exo = {
        1:CodeCarte,
        2:SommesNum,
        3:Exo_Expo,
       
    }  
    
def ChoisirExo():
    print("""Exo : 
          1- Code Carte
          2- Sommes 
          3- Approximation exposant
          4- Dictionnaire Pays 
          5- Filtrage
          6-Sommes Vecteurs
          7- Fichier Python
          """)
    ChoixExo = int(input("Quel exercice voulez vous ouvrir ?"))
    dict_Exo.get(ChoixExo)()
    
def main():
    ChoisirExo()    

if __name__=='__main__':
    main()