

def change(x):
    if x == 0:
        return 1
    else:
        return 0
    
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
        place = int(input("where you place p1 between 1 to 7 "))
    else:
        place = int(input("where you place p2 between 1 to 7 "))
        
    if place < 1 or place > 7:
        print("Invalid input. Please choose a column between 1 and 7.")
        continue

    if essay[place - 1] >= cols:
        print("Column full. Please choose another column.")
        continue

    lists[str(place)][cols - 1 - essay[place - 1]] = 1 if player == 0 else 2
    essay[place - 1] += 1


    for j in range(42):
        resultat = lignedequatre(lists['1'], lists['2'], lists['3'], lists['4'], lists['5'], lists['6'], lists['7'])
    player = change(player)


for col in range(cols):
    for key in lists: 
        print(lists[key][col], end=" ")
    print("")

print("Player", 1 if player == 1 else 2, "win !")