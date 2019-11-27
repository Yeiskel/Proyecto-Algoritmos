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
        boton("Jugar",400,250,100,50,BLACK, GREEN,None)

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
    textrect.center = ((x +(ancho//2)), y + (alto//2))
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
    respuesta = (0<fila and fila<9) and (0<columna and columna<9) and tablero[fila][columna]==0 
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

tablero = inicializar_tablero()
print(visualizacion_tablero(tablero))
  
pygame.init()
pygame.display.set_caption("Reversi")
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
Fuente = pygame.font.SysFont('Helvetica', 30, 5)

screen = pygame.display.set_mode(TAMAÑO)

dibujar_menu()


# Todas las patidas que se quieran jugar 
while True:          #Quitar y re-identar o convertir en funcion(complicado)
    game_over = False                              
    turno = 1
    contador_ficha = FICHAS_INICIALES
    tablero = inicializar_tablero()
    dibujar_tablero(tablero)
    pygame.display.update()
    
    # Un juego completo
    while not game_over:
        
        # Es un jugada
        #while True:
        for event in pygame.event.get():
            #event= pygame.event.wait()
            if event.type == pygame.QUIT:
                game_over=True
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_a: #columnas
                    columna = 1
                elif event.key == pygame.K_b:
                    columna = 2
                elif event.key == pygame.K_c:
                    columna = 3
                elif event.key == pygame.K_d:
                    columna = 4
                elif event.key == pygame.K_e:
                    columna = 5
                elif event.key == pygame.K_f:
                    columna = 6
                elif event.key == pygame.K_g:
                    columna = 7
                elif event.key == pygame.K_h:
                    columna = 8

                if event.key == pygame.K_1: #filas
                    fila = 1
                    if es_valida(fila,columna):
                        realizar_jugada(fila,columna, tablero)
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_2:
                    fila = 2
                    if es_valida(fila,columna):
                        realizar_jugada(fila,columna, tablero)
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_3:
                    fila = 3
                    if es_valida(fila,columna):
                        realizar_jugada(fila,columna, tablero)
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_4:
                    fila = 4
                    if es_valida(fila,columna):
                        realizar_jugada(fila,columna, tablero)
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_5:
                    fila = 5
                    if es_valida(fila,columna):
                        realizar_jugada(fila,columna, tablero)
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_6:
                    fila = 6
                    if es_valida(fila,columna):
                        realizar_jugada(fila,columna, tablero)
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")    
                elif event.key == pygame.K_7:
                    fila = 7
                    if es_valida(fila,columna):
                        realizar_jugada(fila,columna, tablero)
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_8:
                    fila = 8
                    if es_valida(fila,columna):
                        realizar_jugada(fila,columna, tablero)
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
            turno +=1
            turno = turno % 2
            contador_ficha += 1
                    
                
        
            #elif event.type == pygame.MOUSEBUTTONDOWN:
             #   break
        """      
        while True:    
        # Turno de los jugadores          
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
        """
        
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
    
    
pygame.quit()