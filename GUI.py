import pygame

BLUE = (100,0,100)
BLACK = (0,0,0)
tamaño_cuadro = 80

pygame.init()
size = (640,640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Reversi")
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.fill(BLACK)
    Fuente = pygame.font.SysFont('Arial', 16)
    Tx = 0
    Ty = 0
    for i in range(1, size[0], tamaño_cuadro + 1):
        for j in range(1, size[1], tamaño_cuadro + 1):
            pygame.draw.rect(screen, BLUE, [i, j, tamaño_cuadro, tamaño_cuadro], 0)
            
            Ty = Ty + 1
            
        Texto = Fuente.render(str(Tx), True, BLACK)
        
        screen.blit(Texto, [i+5,2])
        screen.blit(Texto, [j,2])

        
        Tx = Tx + 1
        Ty = 0
        
    pygame.display.flip()
    clock.tick(1)
pygame.quit()