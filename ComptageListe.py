def ComptageListe(L,val):
    resultat = 0
    i = 0
    for t in range(len(L)):
        if val == L[i]:
            resultat = resultat + 1
        i = i+1
    return resultat
