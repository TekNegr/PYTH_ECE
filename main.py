import random

def CreateRandomList():
    List = []
    for i in range(1,11):
        NUMA = random.randint(0, 100)
        if NUMA ==0:
            ADD = "Le KAKA"
        else : 
            ADD = NUMA
        List.append(ADD)
    return List

def VerifInList(Nigra):
    List = CreateRandomList()
    if Nigra in List:
       print("C'est gagné")
    else : 
        print(f"Aie Aie t'y etais presque voici la liste : {List}")
       
       
def OrderList(Arg_Liste):
    RAM = []
    Order = 0
    Ordered = False
    while Ordered == False:
        for i in range(Arg_Liste):
            print("kk")
        
            


def main():
    liste = [1,2,3,4,5,6,7,8,9,10]
    print(liste[:1])
    
if __name__=='__main__':
    main()