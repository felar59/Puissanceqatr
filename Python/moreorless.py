import random



hide = random.randint(0,1000)
x = 0
while int(x) != hide:
    x = input("donne un nombre ")
    if int(x) < hide:
        print("C'est +")
    else: 
        print("C'est -")

print("Trouvé c'était", hide)


