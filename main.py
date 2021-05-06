import random

MOVIMIENTOS = {
    'no se mueve':0,
    'salta un metro':1,
    'salta dos metros':2,
}


def main():
    print("Juego de 2 Ranas")
    start = input("¿Desea inicar el juego? (y/n) :").lower()
    if start == 'y':
        rana_1 = 0
        rana_2 = 0
        salto_rana_1 = 0
        salto_rana_2 = 0
        while rana_1 <= 20 or rana_2 <= 20:
            restart = random.randint(1,2)
            if restart == 1:
                rana_1 +=1
                random_movimientos = list(random.choice(list(MOVIMIENTOS.items())))
                salto_rana_1+=random_movimientos[1]
                if rana_1 == 20:
                    break
            else:
                rana_2 +=1
                random_movimientos = list(random.choice(list(MOVIMIENTOS.items())))
                salto_rana_2+=random_movimientos[1]
                if rana_2 == 20:
                    break
        
        if rana_1 >= rana_2:
            print(f"La rana 1 ha ganado y salto:{salto_rana_1}")
        else:
            print(f"La rana 2 ha ganado y salto:{salto_rana_2}")
    else:
        print("Fin del juego")



if __name__ == "__main__":
    main()