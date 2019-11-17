import pygame
import sys

tablero= [[0 for i in range (0,8)] for j in range(0,8)]
    

def visualizacion_tablero (copia_tablero:[int])->list:
    copia_tablero = ""
    k = 0
    while k<8:
        copia_tablero = copia_tablero + "\n" + str(tablero[k])
        k += 1  
    return copia_tablero

def dibujar_tablero(tablero):
    
    screen.fill(GRAY)
    for c in range(8):
        for f in range(8):
            pygame.draw.rect(screen, BLUE, (c*TAMAÑO_CUADRO, f*TAMAÑO_CUADRO, TAMAÑO_CUADRO, TAMAÑO_CUADRO),2)
            if tablero[c][f] == 1:
                pygame.draw.circle(screen,WHITE, (int(c*TAMAÑO_CUADRO+TAMAÑO_CUADRO/2), int(f*TAMAÑO_CUADRO+TAMAÑO_CUADRO/2)), 30)
            elif tablero[c][f] == 2:
                pygame.draw.circle(screen,BLACK, (int(c*TAMAÑO_CUADRO+TAMAÑO_CUADRO/2), int(f*TAMAÑO_CUADRO+TAMAÑO_CUADRO/2)), 30)
    pygame.display.update()

def Realizar_jugada(columna:int,fila:int ):
    if turno == 0:
        tablero[columna][fila]=1
    else:
        tablero[columna][fila]= 2

def jugada_valida(columna:int ,fila:int):
    return tablero[columna][fila]==0

print(visualizacion_tablero(tablero))
game_over = False
turno = 0

pygame.init()
TAMAÑO_CUADRO = 100
BLUE = (0,0,200)
GRAY = (100,100,100)
BLACK =(0,0,0)
WHITE = (255, 255, 255)
ancho = 8 * TAMAÑO_CUADRO
alto = 8 * TAMAÑO_CUADRO
size = (ancho, alto)
Fuente = pygame.font.SysFont('Arial', 16)

screen = pygame.display.set_mode(size)
dibujar_tablero(tablero)
pygame.display.update()


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Jugadores
    
    if turno == 0:
        fila = int(input("Jugador 1, fila: "))
        columna = int(input("Jugador 1, columna: "))
        
    else:
        fila = int(input("Jugador 2, fila: "))
        columna = int(input("Jugador 2, columna: "))
    
    if jugada_valida(columna ,fila):
        Realizar_jugada(columna ,fila)
    turno +=1
    turno = turno % 2
    
    
    print(visualizacion_tablero(tablero))
    dibujar_tablero(tablero)
pygame.quit()
