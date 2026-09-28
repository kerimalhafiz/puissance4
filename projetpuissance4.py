def grille():
    return [[0 for _ in range(7)] for _ in range(6)]  

def choice_column(grille, joueur):
    colonne = int(input(f"Joueur {joueur}, dans quelle colonne souhaitez-vous empiler votre pion ? "))
    if 0 <= colonne <= 6 and grille[0][colonne] == 0:
        for ligne in range(5, -1, -1):
            if grille[ligne][colonne] == 0:
                grille[ligne][colonne] = joueur
                return (ligne, colonne)
    else:  
        print("Colonne invalide ou pleine. Essayez encore.")
        return choice_column(grille, joueur)

def check_winner(grille, joueur, dernier_coup):
    ligne, colonne = dernier_coup

    def compter_direction(c_ligne, c_colonne):
        compteur = 0
        i, j = ligne, colonne
        while 0 <= i < 6 and 0 <= j < 7 and grille[i][j] == joueur:
            compteur += 1
            i += c_ligne
            j += c_colonne
        return compteur

    vertical = compter_direction(1, 0) + compter_direction(-1, 0) - 1
    horizontal = compter_direction(0, 1) + compter_direction(0, -1) - 1
    diagonale_droite = compter_direction(1, 1) + compter_direction(-1, -1) - 1
    diagonale_gauche = compter_direction(1, -1) + compter_direction(-1, 1) - 1
    if vertical >= 4 or horizontal >= 4 or diagonale_droite >= 4 or diagonale_gauche >= 4:
        return True
    else:
        return False  

def afficher_grille(grille):
    print("  ".join(map(str, range(7))))  
    for ligne in grille:
        for case in ligne:
            if case == 1:
                print("\x1b[31m\u25CF\x1b[0m", end="  ")  
            elif case == 2:
                print("\x1b[33m\u25CF\x1b[0m", end="  ")  
            else:
                print("\x1b[90m\u25CB\x1b[0m", end="  ")  
        print()

def jouer():
    g = grille()
    joueur = 1
    partie_terminee = False

    while partie_terminee == False: 
        afficher_grille(g)
        coup = choice_column(g, joueur)
        if check_winner(g, joueur, coup):  
            afficher_grille(g)
            print(f"Félicitations ! Le joueur {joueur} a gagné !")
            partie_terminee = True
        else:  
            if joueur == 1:
                joueur = 2
            else:
                joueur = 1

jouer()
