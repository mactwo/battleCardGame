import random

def comparer_cartes(carte1, carte2): #fonction permet de comparer deux cartes en entrée
    valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}
    valeur_carte1 = valeurs[carte1.valeur]
    valeur_carte2 = valeurs[carte2.valeur]
    if valeur_carte1 > valeur_carte2: #compare les valeurs après avoir assigné avec un tableau de puissance des cartes
        return 1
    elif valeur_carte1 < valeur_carte2:
        return 2
    else:
        return 0

class Carte: #classe qui permet d'associer chiffre et couleur
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
    
class JeuDeCartes: #class générant le jeu de crate entier sans les jockers
    def __init__(self):
        self.valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        self.couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        self.cartes = [Carte(valeur, couleur) for valeur in self.valeurs for couleur in self.couleurs]
        random.shuffle(self.cartes)
    
    def __str__(self):
        return f"{self.cartes}"
    
    def Distribuer(self): #distruibuer les cartes jusqu'à ce qu'il ny en ait plus
        if len(self.cartes) > 0:
            return self.cartes.pop()
        else:
            return None
        
class Joueur: #classe de profil du joueur, fonction pour ajouter ou perdre une carte
    def __init__(self, nom):
        self.nom = nom
        self.main = []
    
    def obtenir_pseudo(self):
        return self.nom

    def ajouter_carte(self, carte):
        if carte:
            self.main.append(carte)

    def retirer_carte(self):
        if len(self.main) > 0:
            return self.main.pop(0)
        else:
            return None


        
        
def jouer_bataille(): #fonction principale duu jeu
    jeu = JeuDeCartes() #appel pour générer le jeu de carte
    joueur1 = Joueur(input("Votre pseudo: ")) #définition des joueurs
    joueur2 = Joueur("IA")

    # Distribution des cartes
    for _ in range(len(jeu.cartes) // 2):
        joueur1.ajouter_carte(jeu.Distribuer())
        joueur2.ajouter_carte(jeu.Distribuer())
    
    #affichage des jeux des joueurs après la distribution
    print("__________________________________")
    print(f"Cartes de {joueur1.obtenir_pseudo()}: {[str(carte) for carte in joueur1.main]}")
    print("__________________________________")
    print(f"Cartes de {joueur2.obtenir_pseudo()}: {[str(carte) for carte in joueur2.main]}")
    print("__________________________________")

    tour = 0
    #boucle limitée à 1000 tours tant qu'il reste toujours des cartes a un joueur, une boucle entière = une manche
    while joueur1.main and joueur2.main and tour < 2000: 
        #tirage et affichage des cartes
        carte_joueur1 = joueur1.retirer_carte()
        carte_joueur2 = joueur2.retirer_carte()
        print(f"Vous avez tiré {carte_joueur1} contre la {carte_joueur2} de l'IA")
        resultat = comparer_cartes(carte_joueur1, carte_joueur2)

        #algorithme perdu/gagné
        if resultat == 1:
            joueur1.ajouter_carte(carte_joueur1)
            joueur1.ajouter_carte(carte_joueur2)
            print(f"Manche gagnée, +2 cartes")
        elif resultat == 2:
            joueur2.ajouter_carte(carte_joueur1)
            joueur2.ajouter_carte(carte_joueur2)
            print(f"Manche perdue, -2 cartes")
        elif resultat == 0:
            print("Manche à égalité")
        print(f"_________{joueur1.obtenir_pseudo()} : {len(joueur1.main)} cartes_____et _____{joueur2.obtenir_pseudo()} : {len(joueur2.main)} cartes___________")
        tour += 1
    
    #vérification à la fin du tour si un joueur a gagné
    if len(joueur1.main) > len(joueur2.main) :
        print(joueur1.obtenir_pseudo()+" a gagné !")
    elif len(joueur2.main) > len(joueur1.main):
        print(joueur2.obtenir_pseudo()+" a gagné !")
    else:
        print("Égalité !")

#lance le jeu
if __name__ == "__main__":
    jouer_bataille()



