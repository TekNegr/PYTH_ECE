class classA():
    def __init__(self,class_n: str):
        self.i = 3
        if class_n != None:
            self.classe = class_n
        else:
            class_n = "A"
      
    def afficher_i():
        print(f"Dans la classe {self.classe}, i = {self.i}")


class classB(classA):
    def __init__(self, class_n:str):
        super().__init__(class_n)
        self.i = 2
        if class_n != None:
            self.classe = class_n
        else:
            class_n = "B"
            
class classC(classB):
    def __init__(self, class_n= "C"):
        super().__init__(class_n)
        self.i = 1
        
    
def main():
    A = classA(None)
    B = classB(None)
    C = classC(None)
    A.afficher_i()
    B.afficher_i()
    C.afficher_i()
    
if __name__ == "__main__":
    main()