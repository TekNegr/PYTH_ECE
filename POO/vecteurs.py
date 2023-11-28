class Point():
    def __init__(self,x:int ,y:int):
        self.x = x
        self.y = y

class Segment():
    def __init__(self, OriX:int, OriY:int, ExtX:int, ExtY:int):
        self.Origine = Point(OriX, OriY)
        self.Extremite = Point(ExtX, ExtY)
        
    def affichage(self):
        print(f"""
              Origine : ({self.Origine.x} ; {self.Origine.y})
              Extremite : ({self.Extremite.x} ; {self.Extremite.y})
              """)
        
def main():
    segment = Segment(5,8,10,5)
    segment.affichage()
    
    
if __name__ =="__main__":
    main()