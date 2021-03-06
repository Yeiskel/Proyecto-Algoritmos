# Autores: Yeiskel Cisneros 14-10223
#           Gerardo Carrillo 15-11662
import pygame
import sys
from random import randint
#-------ULTIMAS FUNCIONES AGREGADAS-----------#

def trad_num_letra(num:int)->str:
    try:
        assert(1<=num<9)
    except:
        print("Error en la asercion de la funcion trad_num_letra()")
    letra=[-1,"A","B","C","D","E","F","G","H"]
    resp=letra[num]
    return resp
def ayuda():
    print("T: Visualizar tablero \nR: Ver jugadas validas \nJ: Ver jugador \nQ: Ayuda \n****************************** ")
def simulador(tablero:list, turno:int, fila:int, columna:int)->bool:
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
        sys.exit()
    estado=False
    direccion = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]             
    # Direcciones: 
    # abajo=[1,0], arriba=[-1,0], derecha=[0,1], izquierda=[0,-1],
    # der_abj=[1,1], der_arrb=[-1,1], izq_abj=[1,-1], izq_arrb=[-1,-1]
    f=0
    while f<8:
        temp_f=direccion[f][0]
        temp_c=direccion[f][1]
        
        pos_f=fila + temp_f
        pos_c=columna + temp_c
        
        while 0<pos_f<9 and 0<pos_c<9 and tablero[pos_f][pos_c]==adversario and tablero[fila][columna]==0:
            pos_f=pos_f + temp_f
            pos_c=pos_c + temp_c
        if 0<pos_f<9 and 0<pos_c<9 and tablero[pos_f][pos_c]==jugador:
            if pos_f!=fila+1 and pos_f!=fila-1 and pos_c!=columna+1 and pos_c!=columna-1:
                estado=True
        f+=1
    return estado
def mov_posibles(copia_tablero:list, turno:int, mensaje:bool)->int:
    jugador = traductor_turno_jugador(turno)
    mov_posibles=0
    if mensaje==True:
        print()
    for fila in range(1,9):
        for columna in range(1,9):
            temp = simulador(copia_tablero, turno, fila, columna)
            if temp==True:
                mov_posibles+=1
                if mensaje==True:
                    print(f"Tablero[{trad_num_letra(columna)}][{fila}]={temp}")
    if mensaje==True:
        print(f"mov. posibles para el jugador {jugador} =", mov_posibles, end="\n\n")
    return mov_posibles        
def matriz_test()->list:  # Matriz aleatoria para testeo
    matriz_test= [[0 for i in range (0,10)] for j in range(0,10)]

    for f in range(1,9):
        for c in range(1,9):
            if matriz_test[f][c]==0:
                matriz_test[f][c]=randint(0,2)
    return (matriz_test)
def contador_fichas(tablero:int, target:int)->int:
    suma=0
    for f in range(1,9):
        for c in range(1,9):
            if tablero[f][c]==target:
                suma+=1
    return suma
def traductor_turno_jugador(turno:int)->int:
    try:
        if turno==0:
            jugador=1
        else:
            jugador=2
        assert((turno==0 and jugador==1) or (turno==1 and jugador==2))
    except:
        print("Error en la asercion de la funcion traductor_turno_jugador()")
        sys.exit()
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
def consumo_fichas(tablero:list, turno:int, fila:int, columna:int)->list:       # Permite consumir las fichas al ser flanqueadas
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
        sys.exit()
    estado=False
    direccion = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]             
    # Direcciones: 
    # abajo=[1,0], arriba=[-1,0], derecha=[0,1], izquierda=[0,-1],
    # der_abj=[1,1], der_arrb=[-1,1], izq_abj=[1,-1], izq_arrb=[-1,-1]
    
    f=0
    casilla=[]       # Almacena una direccion y una casilla verificada a la vez en la forma [d,d,c,c]
    recorrido=[]     # Almacena todas las casillas convertidas sin importar si al final de la linea hay otro numero
    correcion=[]     # Almacena todas las casillas convertidas de vuelta para corregir el punto anterior
    while f<8:
        temp_f=direccion[f][0]
        temp_c=direccion[f][1]
        
        pos_f=fila + temp_f
        pos_c=columna + temp_c
        
        while 0<pos_f<9 and 0<pos_c<9 and tablero[pos_f][pos_c]==adversario and tablero[fila][columna]==0:
            # Muestra las casillas recorridas por cada direccion (testeo)
            casilla=[]
            casilla.append(direccion[f][0])
            casilla.append(direccion[f][1])
            casilla.append(pos_f)
            casilla.append(pos_c)
            recorrido.append(casilla)
            #------------------------------------------------------------
            tablero[pos_f][pos_c]=jugador
            print(f"Recorrido({direccion[f][0]},{direccion[f][1]}): [{trad_num_letra(pos_c)}],[{pos_f}]")
            pos_f=pos_f + temp_f
            pos_c=pos_c + temp_c
        if 0<pos_f<9 and 0<pos_c<9 and tablero[pos_f][pos_c]==jugador:
            if pos_f!=fila+1 and pos_f!=fila-1 and pos_c!=columna+1 and pos_c!=columna-1:
                estado=True
        else:
            pos_f = fila+temp_f
            pos_c = columna+temp_c
            
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
        print(f"Consumo({consumo[i][0]},{consumo[i][1]}): [{trad_num_letra(consumo[i][3])}],[{consumo[i][2]}]")
    # visualizacion_tablero(consumo)
    estado_tablero=[estado, tablero]
    return estado_tablero
#------------REPRESENTACION GRAFICA -----------#
def dibujar_menu():     # Despliega el menú de inicio del juego               
    over = False
    while not over:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 400 + 100 > mouse[0] > 400 and 250 + 50 > mouse[1] > 250:
                    over=True

        pygame.draw.rect(screen, LIGHT_BLUE,(250,100,400,400),15)
        pygame.draw.rect(screen, LIGHT_BLUE,(275,125,350,350),10)            
        pygame.draw.rect(screen, GRAY,(300,150,300,300),0)
        dibujar_cuadros_texto("REVERSI", 400, 170, 100, 50, fuente, GREEN)
        
        #Boton de Jugar
        boton("Jugar",400,250,100,50,BLACK, LIGHT_BLUE,juego_completo)
        #Boton de Salir
        boton("Salir", 400, 350, 100, 50, BLACK, LIGHT_BLUE,quit)
        
        pygame.display.update()      
def otra_partida():     # Permite jugar una nueva partida                 
    over = False
    while not over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                over=True
        
        #Boton de Jugar de nuevo
        boton("Jugar de nuevo",620,150,250,50,BLACK, GREEN,juego_completo)
        #Boton de Salir
        boton("Salir", 700, 225, 100, 50, BLACK, GREEN,quit)
       
        pygame.display.update()    
def boton(mensaje:str, x:int, y:int, ancho:int, alto:int, color_activo:tuple, color_inactivo:tuple, comando=None):  #Crea botones funcionales 
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + ancho > mouse[0] > x and y + alto > mouse[1] > y:
            pygame.draw.rect(screen, color_activo, (x,y,ancho,alto),0)
            if click[0] == 1 and comando != None:
                comando() 
    else:
            pygame.draw.rect(screen, color_inactivo, (x,y,ancho,alto),0)
    dibujar_cuadros_texto(mensaje, x, y, ancho, alto, fuente, WHITE)          
def dibujar_cuadros_texto(mensaje:str, x:int, y:int, ancho:int, alto:int, fuente, color:tuple): #Permite visualizar texto dentro del juego
    textscreen = fuente.render(mensaje, True, color)
    textSurf = textscreen
    textrect = textscreen.get_rect()
    textrect.center = ((x +(ancho//2)), y + (alto//2))
    screen.blit(textSurf,textrect)  
def cuadro_jugador(turno:int):  #Muestra el turno y nombre del jugador
    if turno==0:
        dibujar_cuadros_texto("Turno de " + jugador_1, 700, 100, 100, 100, fuente, BLACK)
    elif turno==1:
        dibujar_cuadros_texto("Turno de " + jugador_2, 700, 100, 100, 100, fuente, WHITE)
def jugada_invalida(invalida:bool):     #Mensaje de error ante una jugada inválida
    if invalida== True:
            dibujar_cuadros_texto("Jugada inválida", 700, 150, 100, 100, fuente, RED)
            dibujar_cuadros_texto("Intente nuevamente", 700, 200, 100, 100, fuente, RED)
    else:
        pass
def instrucciones(game_over):   #Especifica la forma en que se debe ingresar las entradas del teclado
    if game_over == False:
        dibujar_cuadros_texto("Ingrese una letra", 700, 250, 100, 100, fuente, LIGHT_GRAY)
        dibujar_cuadros_texto("y luego un número", 700, 300, 100, 100, fuente, LIGHT_GRAY)
    elif game_over == True:
        pass  
def dibujar_tablero(tablero:list ,turno:int, invalida:bool, game_over:bool):    #Dibuja el tablero con todos sus elementos sobre la interfaz
    screen.fill(GRAY)
    letras = ["0","A","B","C","D","E","F","G","H", ""]
    n = 1
    dibujar_cuadros_texto("REVERSI", 700, 40, 100, 50, fuente, GREEN)
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
                pygame.draw.circle(screen, WHITE, (COORDENADA_X, COORDENADA_Y), 20)
        #Coordenadas graficas del tablero
        texto = fuente.render(letras[f], True, WHITE)
        texto2 = fuente.render(str(n), True, WHITE)
        screen.blit(texto, [f*TAMAÑO_CUADRO + 20,15])
        screen.blit(texto, [(f*TAMAÑO_CUADRO) + 20, 550])
        if f!= 0:
            screen.blit(texto2,[25,f*TAMAÑO_CUADRO +10])
            screen.blit(texto2,[560,f*TAMAÑO_CUADRO +10])
        cuadro_jugador(turno)
        jugada_invalida(invalida)
        instrucciones(game_over)

        n += 1
    if game_over == True:   # parametro 828
            for k in range(50):
                resultados(tablero, (828-50)+k) 
            otra_partida()      
    else:
        pass 
    pygame.display.update()
def tablero_consola(tablero:[int])->str:    # Muestra en consola la matriz de forma ordenada     
    copia_tablero = ""
    k = 0
    while k<8:
        copia_tablero = copia_tablero + "\n" + str(tablero[k])
        k += 1  
    return print(copia_tablero, end="\n\n")
#---------------ESTRUCTURA INTERNA -------------#
def inicializar_tablero()->list:
    tablero= [[0 for i in range (0,10)] for j in range(0,10)]    # Creacion del tablero de 8x8 sin fichas
    # Fichas iniciales
    tablero[4][4] = tablero[5][5] = 1
    tablero[5][4] = tablero[4][5] = 2
    return(tablero)    
def es_valida(copia_tablero:list, tablero:list, turno:int, fila:int, columna:int)->bool:    # Verifica que una jugada es válida 
    print(f"\nPosicion jugada= [{trad_num_letra(columna)}],[{fila}]")
    estado_tablero=consumo_fichas(copia_tablero, turno, fila, columna)
    respuesta = (0<fila and fila<9) and (0<columna and columna<9) and copia_tablero[fila][columna]==0 and estado_tablero[0]
    copia_tablero=tablero[:]
    return respuesta
def realizar_jugada(copia_tablero:list, turno:int, fila:int, columna:int)->'void':      # Modifica la matriz con la jugada deseada  
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
def cambiar_turno(turno:int)->int:      #Alterna los turnos de los jugadores
    if turno==0:
        turno=1        # Jugador 2/blancas
    else:
        turno=0        # Jugador 1/negras
    return turno
def resultados(tablero:list, par_mov:int)->str:     # Muestra los resultados y el ganador
    fichas_negras = contador_fichas(tablero, 1) 
    fichas_blancas = contador_fichas(tablero, 2)
    print("\nEl numero de fichas del jugador 1 es: " +str(fichas_negras))
    dibujar_cuadros_texto("Fichas totales", 650, 350, 200, 100, fuente, LIGHT_GRAY)
    dibujar_cuadros_texto(jugador_1 + ": ", 700-22, 400, 100, 100, fuente, DARK_GRAY) 
    pygame.draw.circle(screen, GRAY, (par_mov-2, 450), 22)    # Elimina el rastro
    pygame.draw.circle(screen, BLACK, (par_mov, 450), 22)     # par_mov=850-22
    dibujar_cuadros_texto(str(fichas_negras), 800-22, 400, 100, 100, fuente, WHITE)
    
    print("El numero de fichas del jugador 2 es: " +str(fichas_blancas))
    dibujar_cuadros_texto(jugador_2 + ": ", 700-22, 450, 100, 100, fuente, DARK_GRAY)
    pygame.draw.circle(screen, GRAY, (par_mov-2, 500), 22) # Elimina el rastro
    pygame.draw.circle(screen, WHITE, (par_mov, 500), 22)  # par_mov=850-22
    dibujar_cuadros_texto(str(fichas_blancas), 800-22, 450, 100, 100, fuente, BLACK)
    if fichas_blancas > fichas_negras:
        print("\nGana el jugador 2")
        #Mensaje de victoria
        dibujar_cuadros_texto("Gana " + jugador_2, 700, 290, 100, 100, fuente, BLACK)

    elif fichas_negras > fichas_blancas:
        print("\nGana el jugador 1")
        #Mensaje de victoria
        dibujar_cuadros_texto("Gana " + jugador_1, 700, 290, 100, 100, fuente, WHITE)
    else:
        print("\nEmpate")
        dibujar_cuadros_texto("Empate", 700, 290, 100, 100, fuente, GREEN)
    pygame.display.update()
#-----------------JUEGO------------------------#
def juego_completo():

    game_over = False      
    turno=0
    invalida = False                        
    
    tablero = inicializar_tablero()                       # Genera el tablero inicial
    tablero_consola(tablero)                              # Muestra el tablero en la consola
    copia_tablero = tablero[:]                            # Realiza una copia del tablero
    dibujar_tablero(tablero,turno,invalida, game_over)    # Representacion grafica del tablero
    pygame.display.update()
    ayuda()
    # Un juego completo
    defecto = 0 
    while not game_over:
        # Es un jugada
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                game_over=True
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if defecto%2==0:      
                    columna = -1        # Valor por defecto de la variable columna     
                else:
                    pass

                if event.key == pygame.K_a: #columnas
                    columna = 1
                    defecto += 1
                elif event.key == pygame.K_b:
                    columna = 2
                    defecto += 1
                elif event.key == pygame.K_c:
                    columna = 3
                    defecto += 1
                elif event.key == pygame.K_d:
                    columna = 4
                    defecto += 1
                elif event.key == pygame.K_e:
                    columna = 5
                    defecto += 1
                elif event.key == pygame.K_f:
                    columna = 6
                    defecto += 1
                elif event.key == pygame.K_g:
                    columna = 7
                    defecto += 1
                elif event.key == pygame.K_h:
                    columna = 8
                    defecto += 1
                elif event.key == pygame.K_r:
                    mov_posibles(tablero, turno, True)
                elif event.key == pygame.K_j:
                    print()
                    print("Turno del jugador " + str(traductor_turno_jugador(turno)))
                elif event.key == pygame.K_t:
                    tablero_consola(tablero)
                elif event.key == pygame.K_q:
                    ayuda()

                if event.key == pygame.K_1 or event.key == pygame.K_KP1: #filas
                    fila = 1
                    if  columna!=-1 and es_valida(copia_tablero, tablero, turno, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        invalida = False
                        defecto += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                        print(f"Error, fila= {fila}, columna= {columna}")
                        invalida= True
                        defecto=0
                        pygame.display.update()
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    fila = 2
                    if  columna!=-1 and es_valida(copia_tablero, tablero, turno, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        invalida = False
                        defecto += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                        print(f"Error, fila= {fila}, columna= {columna}")
                        invalida= True
                        defecto=0
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    fila = 3
                    if  columna!=-1 and es_valida(copia_tablero, tablero, turno, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        invalida = False
                        defecto += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                        print(f"Error, fila= {fila}, columna= {columna}")
                        invalida= True
                        defecto=0
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    fila = 4
                    if  columna!=-1 and es_valida(copia_tablero, tablero, turno, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        invalida = False
                        defecto += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                        print(f"Error, fila= {fila}, columna= {columna}")
                        invalida= True
                        defecto=0
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    fila = 5
                    if  columna!=-1 and es_valida(copia_tablero, tablero, turno, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        invalida = False
                        defecto += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                        print(f"Error, fila= {fila}, columna= {columna}")
                        invalida= True
                        defecto=0
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    fila = 6
                    if  columna!=-1 and es_valida(copia_tablero, tablero, turno, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        invalida = False
                        defecto += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                        print(f"Error, fila= {fila}, columna= {columna}")
                        invalida= True
                        defecto=0
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    fila = 7
                    if  columna!=-1 and es_valida(copia_tablero, tablero, turno, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        invalida = False
                        defecto += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                        print(f"Error, fila= {fila}, columna= {columna}")
                        invalida= True
                        defecto=0
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    fila = 8
                    if  columna!=-1 and es_valida(copia_tablero, tablero, turno, fila, columna):
                        realizar_jugada(copia_tablero, turno, fila, columna)
                        consumo_fichas(copia_tablero, turno, fila, columna)
                        tablero = copia_tablero
                        turno = cambiar_turno(turno)
                        invalida = False
                        defecto += 1
                        break
                    else:
                        print("\nJugada invalida. Intente nuevamente.")
                        print(f"Error, fila= {fila}, columna= {columna}")
                        invalida= True
                        defecto=0
        
        if mov_posibles(tablero, turno, False)==0:
            turno=cambiar_turno(turno)
            print("El jugador actual no tiene movimientos validos, debe mover el otro jugador")        
                        
        # Visualizacion del tablero por jugada    
        dibujar_tablero(tablero,turno, invalida, game_over)
        # Determina cuando finaliza el juego
        if contador_fichas(tablero, 0)==0 or (mov_posibles(tablero, 0, False)==0 and mov_posibles(tablero, 1, False)==0):
            game_over= True
            turno=2
    pygame.display.update()        
    # Visualizacion final de tablero
    tablero_consola(tablero)
    # Muestra los resultados y el ganador
    print("Fichas iniciales: ",FICHAS_INICIALES)
    print("Total casillas: ",TOTAL_CASILLAS) 
    dibujar_tablero(tablero,turno, invalida, game_over)
  
pygame.init()
pygame.display.set_caption("REVERSI".center(270))   #Titulo del juego en la ventana

# CONSTANTES INICIALIZADAS 
TAMAÑO_CUADRO = 60  
GREEN =(67,160,71)      
BLUE = (42,17,204)
LIGHT_BLUE = (50,141,216)
RED = (255,128,0)                        
GRAY = (38,53,69)
LIGHT_GRAY = (192,192,192)
DARK_GRAY = (128,128,128)                                             
BLACK =(0,0,0)                        # Color de fichas jugador 1 y otros elementos de la interfaz 
WHITE = (255, 255, 255)               # Color de fichas jugador 2, fuentes y otros elementos de la interfaz 

ANCHO = (10 * TAMAÑO_CUADRO) + 300
ALTO = 10 * TAMAÑO_CUADRO
TAMAÑO = (ANCHO, ALTO)                                # Tamaño en pixeles del tablero
FICHAS_INICIALES = 4                                  # Numero de fichas al inicio del juego
TOTAL_CASILLAS = FICHAS_INICIALES + 60
fuente = pygame.font.SysFont('Helvetica', 30, 5)      # Configuracion de la fuente usada en el juego
while True:
    try:
        jugador_1 = input('Ingrese el nombre del jugador 1: ')  #Ingreso de los nombres de los jugadores
        jugador_2 = input('Ingrese el nombre del jugador 2: ')
        assert(len(jugador_1) < 10 and len(jugador_2) < 10)
        break
    except:
        print("Los nombres deben constar de menos de 10 caracteres. Intente de nuevo")
screen = pygame.display.set_mode(TAMAÑO)              # Configuracion inicial de la ventana de juego

dibujar_menu()           # Representacion grafica del menu con las opciones JUGAR/SALIR                               

