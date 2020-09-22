import random 

nb = 0
tirage=[]

liste=[i for i in range(1,50)]

for i in range (6) :
    nb = (random.choice(liste))
    tirage.append(nb)
    liste.remove(nb)
        
print (tirage)
print (random.choice(liste))



ListeD= [1,8,2,1,6,5,6,6,3,35,63,2,65,9,2,2]
ListeS= []

def doublon(ListeD): 
    for i in range(len(ListeD)):
        if [i] in ListeD:
            ListeS.append
            
print (ListeS)
        
        
    