#Intento de funcion para jugar reversi, reversa o como sea que se llame

def visualizacion_tablero (copia_tablero:[int])->list:
    copia_tablero = ""
    k = 0
    while k<8:
        copia_tablero = copia_tablero + "\n" + str(tablero[k])
        k += 1  
    return copia_tablero

def seleccion_casilla (fila:int, columna:int, jugador:bool)->'void':
    if jugador_1 == True:
        tablero[fila][columna]=1
    elif jugador_2 == True:
        tablero[fila][columna]=2

def contador_fichas (tablero:[int])-> [int]:
    cero = 0
    numero_fichas_1 = 0
    numero_fichas_2 = 0
    for i in range (0,8):
        for j in range (0,8):
            if tablero[i][j] == 1: 
                numero_fichas_1 += 1
            elif tablero [i][j] == 2:
                numero_fichas_2 += 1
            else:
                cero += 1
    total_fichas_tablero = [numero_fichas_1, numero_fichas_2, cero]
    
    return total_fichas_tablero

def ganador (total_fichas_tablero:[int])->str:
    if total_fichas_tablero[0]>total_fichas_tablero[1] and total_fichas_tablero[0]+total_fichas_tablero[1]==64:
        mensaje = "\nJugador 1 gana"
    elif total_fichas_tablero[1]>total_fichas_tablero[0] and total_fichas_tablero[0]+total_fichas_tablero[1]==64:
        mensaje = "\nJugador 2 gana"
    elif total_fichas_tablero[1]==total_fichas_tablero[0] and total_fichas_tablero[0]+total_fichas_tablero[1]==64:
        mensaje = "\nEmpate entre ambos jugadores"
    else: 
        mensaje = "\nError, aun queda mas jugadas por realizar"
    return mensaje


# CONSTANTES
TOTAL_JUGADAS = 65      # int // Total de jugadas a realizar

# VARIABLES INICIALIZADAS
tablero= [[0 for i in range (0,8)] for j in range(0,8)]        # list // Representacion matricial del tablero
fin_partida = False                                            # bool // Indica el estado actual de la partida
jugador_1 = True                                               # bool // Indica cuando el jugador 1 juega  
jugador_2= False                                               # bool // Indica cuando el jugador 2 juega
numero_jugadas = 0                                             # int  // Lleva la cuenta de cuantas jugadas se han realizado

print(visualizacion_tablero(tablero))                          # Primera visualizacion del tablero                   

while fin_partida == False:

    if (jugador_1 == True) and (numero_jugadas < TOTAL_JUGADAS):
        print("\nTurno del jugador 1: ")
        print("Jugada #", numero_jugadas)
        while True:
            try: 
                fila = int(input("Fila: "))
                columna = int(input("Columna: ")) 
                assert ( (fila>=0 and fila<=8) and 
                         (columna>=0 and columna<=8) and
                         tablero[fila][columna] == 0)
                break
            except:
                print("Jugada no valida, intente nuevamente.")
        seleccion_casilla( fila, columna, jugador_1 )                        
        jugador_1 = False
        jugador_2 = True
        numero_jugadas += 1
        print(visualizacion_tablero(tablero))
        
    elif (jugador_2 == True) and (numero_jugadas < TOTAL_JUGADAS):
        print("\nTurno del jugador 2: ")
        print("Jugada #", numero_jugadas)
        while True:
            try: 
                fila = int(input("Fila: "))
                columna = int(input("Columna: ")) 
                assert ( (fila>=0 and fila<=8) and 
                         (columna>=0 and columna<=8) and 
                         tablero[fila][columna] == 0)
                break
            except:
                print("Jugada no valida, intente nuevamente.")
        
        seleccion_casilla( fila, columna, jugador_1 ) 
        jugador_2 = False
        jugador_1 = True
        numero_jugadas += 1
        print(visualizacion_tablero(tablero))

    else:
        fin_partida = True
        
total_fichas_tablero = contador_fichas(tablero)
print()
print(total_fichas_tablero)
print(ganador(total_fichas_tablero))



