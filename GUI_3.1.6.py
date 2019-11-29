import pygame
import sys
#-------ULTIMAS FUNCIONES AGREGADAS-----------#
def traductor_turno_jugador(turno:int)->int:

    try:
        if turno==0:
            jugador=1
        else:
            jugador=2
        assert((turno==0 and jugador==1) or (turno==1 and jugador==2))
    except:
        print("Error en la asercion de la funcion traductor_turno_jugador()")
    return jugador

def elimina_num_lista(y:list, n:int)->list:
    copia_y=[]
    for k in range(len(y)):
        if n==y[k]:
            pass
        else:
            copia_y.append(y[k])
    return copia_y

def diferencia_listas(y:list, x:list)->list:
    for k in range(len(x)):
        y=elimina_num_lista(y,x[k])
    return y

def consumo_fichas(tablero:list, turno:int, fila:int, columna:int)->list:
    try:
        if turno==0:
            jugador=1        # Turno 0/Jugador 1/negras
            adversario=2
        else:
            jugador=2        # Turno 1/Jugador 2/blancas
            adversario=1
        assert( (turno==0 and jugador==1 and adversario==2) or (turno==1 and jugador==2 and adversario==1) )    
    except:
        print("Error en la asercion para los siguientes valores: ")
        print("turno: "+str(turno)+" ,jugador: "+str(jugador)+", adversario: "+str())
        
    estado=False
    direccion = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]             
    # Direcciones: 
    # abajo=[1,0], arriba=[-1,0], derecha=[0,1], izquierda=[0,-1],
    # der_abj=[1,1], der_arrb=[-1,1], izq_abj=[1,-1], izq_arrb=[-1,-1]
   
    
    f=0
    casilla=[]       # Almacena una direccion y una casilla verificada a la vez en la forma [d,d,c,c]
    recorrido=[]     # Almacena todas las convertidas sin importar si al final de la linea hay otro numero
    correcion=[]     # Almacena todas las casillas convertidas de vuelta para corregir el punto anterior
    print(f"inicio: tablero[{fila}][{columna}]")
    while f<8:
        temp_f=direccion[f][0]
        temp_c=direccion[f][1]
        
        pos_f=fila + temp_f
        pos_c=columna + temp_c
        
        while 0<pos_f<9 and 0<pos_c<9 and tablero[pos_f][pos_c]==adversario:
            # Muestra las casillas recorridas por cada direccion (testeo)
            casilla=[]
            casilla.append(direccion[f][0])
            casilla.append(direccion[f][1])
            casilla.append(pos_f)
            casilla.append(pos_c)
            recorrido.append(casilla)
            #------------------------------------------------------------
            tablero[pos_f][pos_c]=jugador
            print(f"Recorrido({direccion[f][0]},{direccion[f][1]}): [{pos_f}],[{pos_c}]")
            pos_f=pos_f + temp_f
            pos_c=pos_c + temp_c
        if 0<pos_f<9 and 0<pos_c<9 and tablero[pos_f][pos_c]==jugador :
            estado=True
        else:
            pos_f=fila + temp_f
            pos_c=columna + temp_c
            
            while 0<pos_f<9 and 0<pos_c<9 and tablero[pos_f][pos_c]==jugador:
                # Muestra las casillas recorridas por cada direccion (testeo)
                casilla=[]
                casilla.append(direccion[f][0])
                casilla.append(direccion[f][1])
                casilla.append(pos_f)
                casilla.append(pos_c)
                correcion.append(casilla)
                #------------------------------------------------------------
                tablero[pos_f][pos_c]=adversario
                pos_f=pos_f + temp_f
                pos_c=pos_c + temp_c
        f+=1
    
    consumo=diferencia_listas(recorrido, correcion)
    
    for i in range(len(consumo)):
        print(f"Consumo({consumo[i][0]},{consumo[i][1]}): [{consumo[i][2]}],[{consumo[i][3]}]")
    # visualizacion_tablero(consumo)
    estado_tablero=[estado, tablero]
    return estado_tablero

#------------REPRESENTACION GRAFICA -----------#
def dibujar_menu():                 
    
    over = False
    
    while not over:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 400 + 100 > mouse[0] > 400 and 250 + 50 > mouse[1] > 250:
                    print("El menu se cerró")
                    over=True
        pygame.draw.rect(screen, GRAY,(300,150,300,300),0)
        
        #Boton de Jugar
        boton("Jugar",400,250,100,50,BLACK, GREEN,juego_completo)

        #Boton de Salir
        boton("Salir", 400, 350, 100, 50, BLACK, GREEN,quit)
       
        pygame.display.update()
def otra_partida():                 
    screen.fill(BLACK)
    over = False
    
    while not over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                over=True
        pygame.draw.rect(screen, GRAY,(300,150,300,300),0)
        
        
        #Boton de Jugar
        boton("Jugar de nuevo",400,250,100,50,BLACK, GREEN,juego_completo)

        #Boton de Salir
        boton("Salir", 400, 350, 100, 50, BLACK, GREEN,quit)
       

        pygame.display.update()    
def boton(mensaje:str, x:int, y:int, ancho:int, alto:int, color_activo:tuple, color_inactivo:tuple, comando=None):  
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + alto > mouse[1] > y:
            pygame.draw.rect(screen, color_activo, (x,y,ancho,alto),0)
            if click[0] == 1 and comando != None:
                comando() 
    else:
            pygame.draw.rect(screen, color_inactivo, (x,y,ancho,alto),0)

    textSurf, textrect = cuadros_texto(mensaje, fuente)
    textrect.center = ((x +(ancho//2)), y + (alto//2))
    screen.blit(textSurf,textrect)          
def cuadros_texto(texto:str, fuente):
    textscreen = fuente.render(texto, True, WHITE)
    return textscreen, textscreen.get_rect()
def cuadro_jugador(turno:int):
    if turno==0:
            textSurf, textrect = cuadros_texto("Turno Jugador 1", fuente)
            textrect.center = ((700 +(100//2)), 300 + (100//2))
            screen.blit(textSurf,textrect)  
            
    elif turno==1:
        textSurf, textrect = cuadros_texto("Turno Jugador 2", fuente)
        textrect.center = ((700 +(100//2)), 300 + (100//2))
        screen.blit(textSurf,textrect)   
def dibujar_tablero(tablero:list ,turno:int):
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
                pygame.draw.circle(screen, BLACK, (COORDENADA_X, COORDENADA_Y), 20)
               
            elif tablero[f][c] == 2:
                pygame.draw.circle(screen,WHITE, (COORDENADA_X, COORDENADA_Y), 20)
        #Coordenadas graficas del tablero
        texto = fuente.render(letras[f], True, WHITE)
        texto2 = fuente.render(str(n), True, WHITE)
        screen.blit(texto, [f*TAMAÑO_CUADRO + 20,15])
        screen.blit(texto, [(f*TAMAÑO_CUADRO) + 20, 550])
        if f!= 0:
            screen.blit(texto2,[25,f*TAMAÑO_CUADRO +10])
            screen.blit(texto2,[560,f*TAMAÑO_CUADRO +10])
        cuadro_jugador(turno)    
        n += 1
    pygame.display.update()
def tablero_consola(tablero:[int])->str:    
    copia_tablero = ""
    k = 0
    while k<8:
        copia_tablero = copia_tablero + "\n" + str(tablero[k])
        k += 1  
    return print(copia_tablero)
#---------------ESTRUCTURA INTERNA -------------#
def inicializar_tablero()->list:
    tablero= [[0 for i in range (0,10)] for j in range(0,10)]    # Creacion del tablero de 8x8 sin fichas
    
    # Fichas iniciales
    tablero[4][4] = tablero[5][5] = 1
    tablero[5][4] = tablero[4][5] = 2
    return(tablero)    
def es_valida(copia_tablero:list, fila:int, columna:int)->bool:
    respuesta = (0<fila and fila<9) and (0<columna and columna<9) and copia_tablero[fila][columna]==0 
    return respuesta 
def realizar_jugada(copia_tablero:list, turno:int, fila:int, columna:int)->'void':  
    try:
        if turno == 0:
            copia_tablero[fila][columna]=1
        else:
            copia_tablero[fila][columna]= 2   
        assert( (copia_tablero[fila][columna]==1 and turno==0) or \
                (copia_tablero[fila][columna]==2 and turno==1) )
    except:
        print("Error en la asercion de la funcion realizar_jugada(), valores: ")
        print("copia_tablero[fila][columna]=", copia_tablero,",turno=",turno)
        sys.exit()
def quedan_fichas(tablero:int)->bool:
    TAMAÑO_TABLERO=8
    i,j,suma,quedan_fichas=0,0,0,True
    while i<TAMAÑO_TABLERO:
        j=0
        while j<TAMAÑO_TABLERO:
            if tablero[i][j]==0:
                suma+=1
    if suma==0:
        quedan_fichas=False
    return quedan_fichas           
def cambiar_turno(turno:int)->int:
    if turno==0:
        turno=1        # Jugador 2/blancas
    else:
        turno=0        # Jugador 1/negras
    return turno
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
        #Mensaje de victoria
        textSurf, textrect = cuadros_texto("Gana el jugador 1", fuente)
        textrect.center = ((700 +(100//2)), 500 + (100//2))
        screen.blit(textSurf,textrect)

    elif fichas_negras > fichas_blancas:
        print("\nGana el jugador 2")
        #Mensaje de victoria
        textSurf, textrect = cuadros_texto("Gana el jugador 2", fuente)
        textrect.center = ((700 +(100//2)), 500 + (100//2))
        screen.blit(textSurf,textrect)
    else:
        print("\nEmpate")
    pygame.display.update()
    input()
#-----------------JUEGO------------------------#
def juego_completo():
    
    game_over = False      
    turno=0                        
    contador_ficha = FICHAS_INICIALES
    
    tablero = inicializar_tablero()             # Genera el tablero inicial
    tablero_consola(tablero)                    # Muestra el tablero en la consola
    copia_tablero = tablero[:]                  # Realiza una copia del tablero
    dibujar_tablero(tablero,turno)              # Representacion grafica del tablero
    pygame.display.update()
    


    # Un juego completo
    while not game_over:
        
        # Es un jugada
        
        for event in pygame.event.get():    
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
                    if es_valida(copia_tablero, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        contador_ficha += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_2:
                    fila = 2
                    if es_valida(copia_tablero, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        contador_ficha += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_3:
                    fila = 3
                    if es_valida(copia_tablero, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        contador_ficha += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_4:
                    fila = 4
                    if es_valida(copia_tablero, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        contador_ficha += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_5:
                    fila = 5
                    if es_valida(copia_tablero, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        contador_ficha += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_6:
                    fila = 6
                    if es_valida(copia_tablero, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        contador_ficha += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")    
                elif event.key == pygame.K_7:
                    fila = 7
                    if es_valida(copia_tablero, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        contador_ficha += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                elif event.key == pygame.K_8:
                    fila = 8
                    if es_valida(copia_tablero, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        contador_ficha += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                print()
                print("Turno del jugador " + str(traductor_turno_jugador(turno)))   
          
          

        # Visualizacion del tablero por jugada
              
        dibujar_tablero(tablero,turno)
        # Determina cuando finaliza el juego
        if contador_ficha == TOTAL_CASILLAS:
            game_over= True
            turno=2
    pygame.display.update()        
    # Visualizacion final de tablero
    tablero_consola(tablero) 
    dibujar_tablero(tablero,turno)
    # Muestra los resultados y el ganador
    print("Fichas iniciales: ",FICHAS_INICIALES)
    print("Total casillas: ",TOTAL_CASILLAS)
    resultados(tablero)

pygame.init()
pygame.display.set_caption("Reversi".center(270))

# CONSTANTES INICIALIZADAS 
TAMAÑO_CUADRO = 60  
GREEN =(67,160,71)      
BLUE = (42,17,204)                    
GRAY = (38,53,69)                                              
BLACK =(0,0,0)                        # Color de fichas jugador 1 y otros elementos de la interfaz 
WHITE = (255, 255, 255)               # Color de fichas jugador 2, fuentes y otros elementos de la interfaz 

ANCHO = (10 * TAMAÑO_CUADRO) + 300
ALTO = 10 * TAMAÑO_CUADRO
TAMAÑO = (ANCHO, ALTO)                                # Tamaño en pixeles del tablero
FICHAS_INICIALES = 4                                  # Numero de fichas al inicio del juego
TOTAL_CASILLAS = FICHAS_INICIALES + 60
fuente = pygame.font.SysFont('Helvetica', 30, 5)      # Configuracion de la fuente usada en el juego
screen = pygame.display.set_mode(TAMAÑO)              # Configuracion inicial de la ventana de juego

dibujar_menu()           # Representacion grafica del menu con las opciones JUGAR/SALIR                               
otra_partida()           # Permite jugar una nueva partida

pygame.quit()