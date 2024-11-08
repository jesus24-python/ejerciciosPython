print("bienvenido al juego de piedra, papel y tijera ")
print("jugador 1, ingresa tu nombre")
nom1 = input()
print ("jugador 2, ingresa tu nombre")
nom2 = input()

print ("el juego quedo:",nom1,  " vs ",nom2)
nom1 =input ("ingresa tu opcion: ")
nom2 =input ("ingresa tu opcion: ")
option = ("piedra")
if  (option == "piedra" and option == "tijeras") or\
    (nom1 == "papel" and nom2 == "piedra") or\
    (nom1 == "tijeras" and nom2 == "papel"):
    print("el ganador es",nom1, option)

elif (nom2 == "piedra" and nom1 == "tijeras") or\
    (nom2 == "papel" and nom1 == "piedra") or\
    (nom2 == "tijeras" and nom1 == "papel"):
    print("el ganador es",nom2)

elif (nom1==nom2):
    print ("empate")





