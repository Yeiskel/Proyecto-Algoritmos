""" 
    demo_modulo_othello.py
    
    DESCRIPCION: Implementacion del algoritmo de conversion de fichas segun las reglas de juego Othello a un puzzle. 
        Reglas: 
            * Tienes solo N turnos para convertir en un tablero aleatorio la mayor cantidad de fichas del adversario.
            * Puedes colocar fichas en cualquier lugar del tablero, sin importar si esta ocupada o no. Si colocas una
              ficha sobre la del adversario esta será convertida en una tuya. 
            * ¡Disfruta!
        Nota: 
            * Por motivos de testeo, se muestra el recorrido que realiza el algoritmo sobre todas las casillas con fichas
              adversarias que estan conectadas a la ficha de la ultima jugada. El recorrido SOLO evalua las posibles fichas
              a convertir. Luego convierte las que cumplen ciertos requisitos.
            * Si lo deseas, puedes cambiar el tamaño del tablero y la cantidad de turnos de las constantes TAMAÑO Y TURNO respectivamente.
    
    Autor: 
        Gerardo Carrillo 
    
    Última modificacion: 24/11/19 (11:40 am)
"""
from random import randint

def cuenta_numero(target:int,tablero:int)->int:
    suma=0
    for f in range(TAMAÑO):
        for c in range(TAMAÑO):
            if tablero[f][c]==target:
                suma+=1
    return suma

def visualizacion_tablero(tablero:[int])->list:    
    copia_tablero = ""
    k = 0
    while k<len(tablero[1]):
        copia_tablero = copia_tablero + "\n" + str(tablero[k])
        k += 1  
    return print(copia_tablero, end="\n\n")

def incializar_tablero(tamaño:int)->list:
    tablero=[[0 for i in range(tamaño)] for j in range(tamaño)]
    for f in range(tamaño):
        for c in range(tamaño):
            tablero[f][c]=randint(0,2)
    return tablero

def adversario(jugador:int)->int:
    if jugador==1:
        adversario=2
    else:
        adversario=1
    return adversario

def msj_error()->str:
    mensaje = "Entrada invalida. Intente nuevamente."
    return print(mensaje)


while True:
    try:
        jugador=int(input("Selecciona tu jugador(1/2): "))
        assert(jugador==1 or jugador==2)
        break
    except:
        msj_error()

# Constantes inicializadas
TAMAÑO=5                       # Tamaño del tablero
TURNOS=2                       # Cantidad de turnos a jugar


adversario = adversario(jugador)                                # Determina quien es el jugador adversario en funcion del jugador actual
print(f"Eres el jugador {jugador}, intenta eliminar la mayor cantidad de numeros {adversario} del tablero en {TURNOS} turnos: ")

tablero = incializar_tablero(TAMAÑO)                            # Inicializa el tablero y sus casillas con valores aleatorios entre 0 y 2
fichas_iniciales_adversario = cuenta_numero(adversario,tablero) # Cuenta la cantidad de fichas del adversario al inicio 
visualizacion_tablero(tablero)                                  # Representacion en consola del tablero

direccion = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]             
# Direcciones: 
# abajo=[1,0], arriba=[-1,0], derecha=[0,1], izquierda=[0,-1],
# der_abj=[1,1], der_arrb=[-1,1], izq_abj=[1,-1], izq_arrb=[-1,-1]


k=0
while k<TURNOS:
    
    print("Fichas del adversario: ", cuenta_numero(adversario,tablero))
    while True:
        try:
            fila_x=int(input("Introduce la fila: "))
            fila_y=int(input("Introduce la columa: "))
            assert(0<=fila_x<TAMAÑO and 0<=fila_y<TAMAÑO)
            break
        except:
            msj_error()
    tablero[fila_x][fila_y]=jugador
    print()
    print("Leyenda: ")
    print("abajo=(1,0), arriba=(-1,0), derecha=(0,1), izquierda=(0,-1), der_abj=(1,1),\nder_arrb=(-1,1), izq_abj=(1,-1), izq_arrb=(-1,-1)")
    print("---------------------------------------------------------------------------")
    f=0
    while f<8:
        temp_x=direccion[f][0]
        temp_y=direccion[f][1]
        pos_x=fila_x
        pos_y=fila_y
        
        pos_x=pos_x + temp_x
        pos_y=pos_y + temp_y

        while 0<=pos_x<TAMAÑO and 0<=pos_y<TAMAÑO and tablero[pos_x][pos_y]==adversario:
            tablero[pos_x][pos_y]=jugador
            print(f"Recorrido({direccion[f][0]},{direccion[f][1]}): [{pos_x}],[{pos_y}]")
            pos_x=pos_x + temp_x
            pos_y=pos_y + temp_y
            
        if 0<=pos_x<TAMAÑO and 0<=pos_y<TAMAÑO and tablero[pos_x][pos_y]==jugador :
            pass
        else:
            pos_x=fila_x
            pos_y=fila_y
            pos_x=pos_x + temp_x
            pos_y=pos_y + temp_y
            
            while 0<=pos_x<TAMAÑO and 0<=pos_y<TAMAÑO and tablero[pos_x][pos_y]==jugador:
                tablero[pos_x][pos_y]=adversario
                pos_x=pos_x + temp_x
                pos_y=pos_y + temp_y
        f+=1
    visualizacion_tablero(tablero)
    k+=1

resultado = fichas_iniciales_adversario - cuenta_numero(adversario, tablero)
print("Fichas inciales: ", fichas_iniciales_adversario)
print("Fichas finales: ", cuenta_numero(adversario,tablero))
print(f"Has convertido {resultado} fichas.")
















