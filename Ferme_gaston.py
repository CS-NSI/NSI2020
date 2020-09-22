ferme_gaston = {'lapin': 5, 'vache': 7,'cochon': 2,'cheval': 4}
BDPrix = {'Sabre laser': 229, 'Etoile ninja': 29.95,'cape': 75, 'Baguette': 35, 'Chapeau': 12, 'Bandeau': 12, 'Balai': 130}

def nb(ferme):
    nombres = 0
    for i in (ferme):
        nombres = nombres + ferme[i]
    return nombres






def nombre_animal(ferme,animal):    
   if animal in ferme:
       return ferme[animal]
   else:
       return 0 
   
    
    
    
   
def dispo(BDPrix, Objet):
    if Objet in BDPrix:
        return True
    else:
        return False
    


    

def PrixMoyen(BDPrix):
    somme = 0
    for i in BDPrix:
        somme = somme + BDPrix[i]
    somme = somme /len(BDPrix)
    return somme
        


def IntervallePrix(PrixMini, PrixMax, BDPrix):
    Intervalle=()
    for i in BDPrix:
        if BDPrix[i] >= PrixMini:
            BDPrix[i] <= PrixMax
            intevalle = BDPrix.Values
    
    
    
    