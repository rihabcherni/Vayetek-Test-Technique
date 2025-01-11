import re
def calculer_somme_etalon(fichier):
    s = 0
    with open(fichier, 'r') as file:
        for i, ligne in enumerate(file, start=1):
            chiffres = re.findall(r'\d', ligne.strip())
            if(len(chiffres) > 0):
                premier = chiffres[0]
                dernier = chiffres[-1]            
                s +=  int(premier + dernier)
    return s
print("La somme totale des valeurs d'étalonnage est :", calculer_somme_etalon("document.txt"))

# ====> La somme totale des valeurs d'étalonnage est : 53386