L=[1,12,15,3]


def PlusPetitElement(L):
    mini = L[0]
    for i in range(len(L)):
        if L[i] < mini:
            mini = L[i]
    return mini

def PlusGrandElement(L):
    maxi = L[0]
    for i in range(len(L)):
        if L[i] > maxi:
            maxi = L[i]
    return maxi