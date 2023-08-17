import pygame
pygame.init()

largeur, hauteur = 1350, 1000
ecran = pygame.display.set_mode((largeur, hauteur))

columnlargeur = largeur // 7

def change(x):
        if x == 0:
            return 1
        else:
            return 0  

def remplisage(listes):
        rows, cols = len(listes[0]), len(listes)

        for col in range(cols): 
            for row in range(rows):
                cercles = [
                    {"position": ((col + 1) * 171.4, (row + 1) * 150), "rayon": 40, "couleur": (255, 0, 0)},
                    {"position": ((col + 1) * 171.4, (row + 1) * 150), "rayon": 50, "couleur": (0, 0, 255)},
                    {"position": ((col + 1) * 171.4, (row + 1) * 150), "rayon": 50, "couleur": (128, 128, 128)},
                ]
                cerclerouge = cercles[0]
                cerclebleu = cercles[1]
                cerclegris = cercles[2]
                if listes[col][row] == 0:
                    couleur = cerclegris["couleur"]
                elif listes[col][row] == 1:
                    couleur = cerclerouge["couleur"]
                elif listes[col][row] == 2:
                    couleur = cerclebleu["couleur"]
                            
                position = cercles[0]["position"]
                rayon = cercles[0]["rayon"]
                pygame.draw.circle(ecran, couleur, position, rayon)

def lignedequatre(*listes):
    rows, cols = len(listes[0]), len(listes)

    #VERTICALE
    for row in range(rows):
        for col in range(cols - 3):
            if listes[col][row] != 0 and listes[col][row] == listes[col + 1][row] == listes[col + 2][row] == listes[col +3 ][row]:
                return True
                
    #HORIZONTAL
    for row in range(rows - 3):
        for col in range(cols):
            if listes[col][row] != 0 and listes[col][row] == listes[col][row + 1] == listes[col][row + 2] == listes[col][row + 3]:
                return True
                
    #DIAGONAL HAUT DROITE
    for col in range(cols):
        for row in range(rows - 3):
            if listes[col][row] != 0 and listes[col][row] == listes[col - 1][row + 1] == listes[col - 2][row + 2] == listes[col - 3][row + 3]:
                return True
                
    #DIAGONAL BAS DROITE
    for col in range(cols - 3):
        for row in range(rows - 3):
            if listes[col][row] != 0 and listes[col][row] == listes[col + 1][row + 1] == listes[col + 2][row + 2] == listes[col + 3][row + 3]:
                return True
                
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    lists = {
        '1': [0, 0, 0, 0, 0, 0],
        '2': [0, 0, 0, 0, 0, 0],
        '3': [0, 0, 0, 0, 0, 0],
        '4': [0, 0, 0, 0, 0, 0],
        '5': [0, 0, 0, 0, 0, 0],
        '6': [0, 0, 0, 0, 0, 0],
        '7': [0, 0, 0, 0, 0, 0]
    }

    essay = [0, 0, 0, 0, 0, 0, 0]
    numberstr = ['1', '2', '3', '4', '5', '6', '7']
    p1 = 0
    p2 = 1
    resultat = False
    player = p1

    while resultat == False:
        cols = len(lists['1'])

        for col in range(cols):
            for key in lists:
                print(lists[key][col], end=" ")
            print("")


        if player == 0:
            place = int(input("(P1 Place your Token Between 1 To 7) : "))
        
        else:
            place = int(input("(P2 Place your Token Between 1 To 7) : "))

        if place < 1 or place > 7:
            print("Invalid input. Please choose a column between 1 and 7.")
            continue

        if essay[place - 1] >= cols:
            print("Column full. Please choose another column.")
            continue

        #Change 0 en 1 ou 2
        lists[str(place)][cols - 1 - essay[place - 1]] = 1 if player == 0 else 2
        essay[place - 1] += 1

        #Design en fonction des 0, 1 et 2
        resultat = remplisage([lists['1'], lists['2'], lists['3'], lists['4'], lists['5'], lists['6'], lists['7']])
        pygame.display.flip()
        
        #Vérifier rangée de 4
        resultat = lignedequatre(lists['1'], lists['2'], lists['3'], lists['4'], lists['5'], lists['6'], lists['7'])

        player = change(player)


    for col in range(cols):
        for key in lists:
            print(lists[key][col], end=" ")
        print("")

    print("Player", 1 if player == 1 else 2, "win !")
pygame.quit()