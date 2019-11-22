"""
    GUI_3.0.py

    DESCRIPCION: Juego de Reversi(Othello)
    
    Autores: 
        Gerardo Carrillo 
        Yeiskel Cisneros
    
    Última modificacion: 20/11/19
"""

import pygame
import sys

def dibujar_menu():
    
    over = False
    
    while not over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over=True
                #pygame.quit()
                #quit()
            
        pygame.draw.rect(screen, GRAY,(300,150,300,300),0)
        
        
        #Boton de Jugar
        boton("Jugar",400,250,100,50,BLACK, GREEN,juego_completo)

        #Boton de Salir
        boton("Salir", 400, 350, 100, 50, BLACK, GREEN,quit)
       

        pygame.display.update()
#Crea un boton con funcionabilidad 
def boton(mensaje:str, x:int, y:int, ancho:int, alto:int, color_activo:tuple, color_inactivo:tuple, comando=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + alto > mouse[1] > y:
            pygame.draw.rect(screen, color_activo, (x,y,ancho,alto),0)
            if click[0] == 1 and comando != None:
                comando() 

    else:
            pygame.draw.rect(screen, color_inactivo, (x,y,ancho,alto),0)

    textSurf, textrect = cuadros_texto(mensaje, Fuente)
    textrect.center = ((x +(ancho/2)), y + (alto/2))
    screen.blit(textSurf,textrect)

                
def cuadros_texto(texto:str, fuente):
    textscreen = fuente.render(texto, True, WHITE)
    return textscreen, textscreen.get_rect()
    

def inicializar_tablero()->'list':
    

    tablero= [[0 for i in range (0,10)] for j in range(0,10)]    # Creacion del tablero de 8x8 sin fichas
    # Fichas iniciales
    tablero[4][4] = tablero[5][5] = 1
    tablero[5][4] = tablero[4][5] = 2
    return(tablero)
    

def visualizacion_tablero(copia_tablero:[int])->list:    
    copia_tablero = ""
    k = 0
    while k<8:
        copia_tablero = copia_tablero + "\n" + str(tablero[k])
        k += 1  
    return copia_tablero

def dibujar_tablero(tablero):
    screen.fill(GRAY)
    letras = ["0","A","B","C","D","E","F","G","H", ""]
    n = 1
    for f in range(1,9):
        for c in range(1,9):
            pygame.draw.rect(screen, GREEN, (c*TAMAÑO_CUADRO, f*TAMAÑO_CUADRO, TAMAÑO_CUADRO, TAMAÑO_CUADRO),0)

    for f in range(1,9):
        for c in range(1,9):
            COORDENADA_X = c*TAMAÑO_CUADRO+TAMAÑO_CUADRO//2
            COORDENADA_Y = f*TAMAÑO_CUADRO+TAMAÑO_CUADRO//2
            
            pygame.draw.rect(screen, BLUE, (c*TAMAÑO_CUADRO, f*TAMAÑO_CUADRO, TAMAÑO_CUADRO, TAMAÑO_CUADRO),2)
            if tablero[f][c] == 1:
                #pygame.draw.circle(screen,BLACK, (int(c*TAMAÑO_CUADRO+TAMAÑO_CUADRO/2), int(f*TAMAÑO_CUADRO+TAMAÑO_CUADRO/2)), 20)
                pygame.draw.circle(screen, BLACK, (COORDENADA_X, COORDENADA_Y), 20)
               
            elif tablero[f][c] == 2:
                pygame.draw.circle(screen,WHITE, (COORDENADA_X, COORDENADA_Y), 20)
        #Coordenadas graficas del tablero
        texto = Fuente.render(letras[f], True, WHITE)
        texto2 = Fuente.render(str(n), True, WHITE)
        screen.blit(texto, [f*TAMAÑO_CUADRO + 20,15])
        screen.blit(texto, [(f*TAMAÑO_CUADRO) + 20, 550])

        if f!= 0:
            screen.blit(texto2,[25,f*TAMAÑO_CUADRO +10])
            screen.blit(texto2,[560,f*TAMAÑO_CUADRO +10])
            
        n += 1
    pygame.display.update()

def es_valida(fila:int, columna:int)->bool:
    respuesta = (0<=fila and fila<8) and (0<=columna and columna<8) and tablero[fila][columna]==0 
    return respuesta 

def realizar_jugada(fila:int, columna:int, tablero)->'void':  
    if turno == 0:
        tablero[fila][columna]=1
    else:
        tablero[fila][columna]= 2

def cambia_color(fila:int,columna:int):  # Novedad proximamente disponible en la actualizacion 3.1
    print(fila,columna)
    
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

def juego_completo():
    game_over = False          
    turno = 0                    
    contador_ficha = FICHAS_INICIALES
    tablero = inicializar_tablero()
    dibujar_tablero(tablero)
    pygame.display.update()
    
    # Un juego completo
    while not game_over:
        

        # Es un jugada
        while not game_over:
            #for event in pygame.event.get():
            event= pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
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
                realizar_jugada(fila,columna, tablero)
                break
            else:
                print("\nJugada invalida. Intente nuevamente.")
        contador_ficha += 1
        turno +=1
        turno = turno % 2
        
        # Visualizacion del tablero por jugada
        print(visualizacion_tablero(tablero))
        dibujar_tablero(tablero)

        # Determina cuando finaliza el juego
        if contador_ficha == TOTAL_CASILLAS:
            game_over= True
            print("If no ignorado")

    # Visualizacion final de tablero 
    dibujar_tablero(tablero)

    # Muestra los resultados y el ganador
    print("Fichas iniciales: ",FICHAS_INICIALES)
    print("Total casillas: ",TOTAL_CASILLAS)
    resultados(tablero)

    while True:
        try: 
            empezar_partida = input("Escriba (S) si desea jugar otra partida o (N) para terminar: ")
            empezar_partida = empezar_partida.upper()
            print(empezar_partida)
            assert(empezar_partida=="S" or empezar_partida=="N")
            break
        except:
            print("Entrada invalida. Intente nuevamente")
"""
while True:
    try:
        empezar_partida = input("¿Desea Jugar? \n(S/N): ")
        empezar_partida = empezar_partida.upper()
        assert(empezar_partida=="S" or empezar_partida=="N")
        break
    except: 
        print("Entrada no valida. Intente nuevamente")
"""    

tablero = inicializar_tablero()
print(visualizacion_tablero(tablero))
  
pygame.init()


# CONSTANTES INICIALIZADAS 
TAMAÑO_CUADRO = 60  
GREEN =(67,160,71)      
BLUE = (42,17,204)                            # Color del borde de los cuadros en el tablero
GRAY = (52,73,94)                        # Color de fondo del tablero
WHITE = (255, 255, 255)                     # Color de las fichas del jugador 1
BLACK =(0,0,0)                              # Color de las fichas del jugador 2
ANCHO = (10 * TAMAÑO_CUADRO) + 300
ALTO = 10 * TAMAÑO_CUADRO
TAMAÑO = (ANCHO, ALTO)                      # Tamaño en pixeles del tablero
FICHAS_INICIALES = 4                        # Numero de fichas al inicio del juego
TOTAL_CASILLAS = FICHAS_INICIALES + 60

turno = 0
Fuente = pygame.font.SysFont('Helvetica', 30, 5)
screen = pygame.display.set_mode(TAMAÑO)

# Primero aparece el menu
dibujar_menu()
juego_completo()


# Ahora aparece el resto del juego
# Todas las patidas que se quieran jugar 

    

pygame.quit()
quit()
