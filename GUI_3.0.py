"""
    GUI_3.0.py

    DESCRIPCION: Juego de Reversi(Othello)
    
    Autores: 
        Gerardo Carrillo 
        Yeiskel Cisneros
    
    Última modificacion: 18/11/19
"""

import pygame
import sys


def visualizacion_tablero(copia_tablero:[int])->list:    
    copia_tablero = ""
    k = 0
    while k<8:
        copia_tablero = copia_tablero + "\n" + str(tablero[k])
        k += 1  
    return copia_tablero

def dibujar_tablero(tablero):
    screen.fill(GRAY)
    letras = ["A","B","C","D","E","F","G","H"]
    n = 0
    for f in range(0,8):
        for c in range(0,8):
            pygame.draw.rect(screen, BLUE, (c*TAMAÑO_CUADRO, f*TAMAÑO_CUADRO, TAMAÑO_CUADRO, TAMAÑO_CUADRO),2)
            if tablero[f][c] == 1:
                pygame.draw.circle(screen,WHITE, (int(c*TAMAÑO_CUADRO+TAMAÑO_CUADRO/2), int(f*TAMAÑO_CUADRO+TAMAÑO_CUADRO/2)), 30)
            elif tablero[f][c] == 2:
                pygame.draw.circle(screen,BLACK, (int(c*TAMAÑO_CUADRO+TAMAÑO_CUADRO/2), int(f*TAMAÑO_CUADRO+TAMAÑO_CUADRO/2)), 30)

        #Coordenadas graficas del tablero
        texto = Fuente.render(letras[f], True, BLACK)
        texto2 = Fuente.render(str(n), True, BLACK)
        screen.blit(texto, [f*100 + 5,2])
        if f!= 0:
            screen.blit(texto2,[5,f*100 +5])
        n += 1
    pygame.display.update()

def realizar_jugada(fila:int, columna:int)->'void':  
    if turno == 0:
        tablero[fila][columna]=1
    else:
        tablero[fila][columna]= 2

def es_valida(fila:int, columna:int)->bool:
    return (0<=fila and fila<8) and (0<=columna and columna<8) and tablero[fila][columna]==0  

def resultados(tablero:list)->str:
    fichas_negras = 0 
    fichas_blancas = 0
    for f in range(8):
        for c in range(8):
            if tablero[f][c] == 1:
                fichas_blancas += 1
            elif tablero[f][c] == 2:
                fichas_negras += 1
    print("\nEl numero de fichas del jugador 1 es: " +str(fichas_blancas))
    print("El numero de fichas del jugador 2 es: " +str(fichas_negras))
    if fichas_blancas > fichas_negras:
        print("\nGana el jugador 1")
    elif fichas_negras > fichas_blancas:
        print("\nGana el jugador 2")
    else:
        print("\nEmpate")

def cambia_color(fila:int,columna:int):  # Novedad proximamente disponible en la actualizacion 2.1
    print(fila,columna)
    


tablero= [[0 for i in range (0,8)] for j in range(0,8)]    # Creacion del tablero de 8x8 sin fichas
# Fichas iniciales
tablero[3][3] = tablero[4][4] = 1
tablero[4][3] = tablero[3][4] = 2

print(visualizacion_tablero(tablero))    
game_over = False                              
turno = 0        

pygame.init()

# CONSTANTES INICIALIZADAS 
TAMAÑO_CUADRO = 100        
BLUE = (0,0,200)              # Color del borde de los cuadros en el tablero
GRAY = (100,100,100)          # Color de fondo del tablero
WHITE = (255, 255, 255)       # Color de las fichas del jugador 1
BLACK =(0,0,0)                # Color de las fichas del jugador 2
ANCHO = 8 * TAMAÑO_CUADRO
ALTO = 8 * TAMAÑO_CUADRO
TAMAÑO = (ANCHO, ALTO)        # Tamaño en pixeles del tablero
CONTADOR_FICHA = 4            # Cuenta el numero de fichas colocadas en el tablero
TOTAL_CASILLAS = 64


Fuente = pygame.font.SysFont('Arial', 16)
screen = pygame.display.set_mode(TAMAÑO)
dibujar_tablero(tablero)
pygame.display.update()


while not game_over:

    while True:
        event= pygame.event.wait()
        if event.type == pygame.QUIT:
            game_over=True
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            break

        
    # Turno de los jugadores
    while True:
        
        if turno == 0:                                    
            # Jugador 1: Fichas blancas
            fila = int(input("Jugador 1, fila: "))
            columna = int(input("Jugador 1, columna: "))
            
        else:                                             
            # Jugador 2: Fichas negras 
            fila = int(input("Jugador 2, fila: "))
            columna = int(input("Jugador 2, columna: "))
            
            # Verificacion de jugada valida
        if es_valida(fila,columna):
            realizar_jugada(fila,columna)
            break
        else:
            print("\nJugada invalida. Intente nuevamente.")
    CONTADOR_FICHA += 1
    turno +=1
    turno = turno % 2
    
    # Visualizacion del tablero por jugada
    print(visualizacion_tablero(tablero))
    dibujar_tablero(tablero)

    # Determina cuando finaliza el juego
    if CONTADOR_FICHA == TOTAL_CASILLAS:
        game_over= True
pygame.quit()
# Visualizacion final de tablero 
dibujar_tablero(tablero)

# Muestra los resultados y el ganador
resultados(tablero)

