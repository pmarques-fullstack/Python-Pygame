# Importar a livraria pygame e inicializa o motor de jogo
import pygame
# Importar a classe paddle
from paddle import Paddle

pygame.init()

# Definir cores
BLACK = (0,0,0)
WHITE = (255,255,255)
OUTRA = (0,255,0)
 
# Criar janela
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Apanh'á Bola")

# Define a cor, largura e altura do paddle
paddleA = Paddle(WHITE, 50, 10)
paddleA.rect.x = 325
paddleA.rect.y = 470

# Cria uma lista que contem todos os sprites que serão utilizados
all_sprites_list = pygame.sprite.Group()
 
# Adiciona o paddle à lista de sprites
all_sprites_list.add(paddleA)
 
# Controlo de loop infinito ou até o utilizador sair do jogo (fecha a janela).
emJogo = True
 
# Cria um clock que será utilizado para controlar a velocidade de refresh
clock = pygame.time.Clock()

score = 0
 
# -------- Ciclo Principal do programa -----------
while emJogo:
    # --- Ciclo principal
    for event in pygame.event.get(): # O utilizador fez alguma coisa
        if event.type == pygame.QUIT: # O utilizador fechou a janela
              emJogo = False # Muda o controlo para assinalar que o jogo terminou
    
    # Move o paddle quando o utilizador pressiona as teclas direccionais esquerda e direita 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddleA.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddleA.moveRight(5)

    # --- Lógica do jogo AQUI
    all_sprites_list.update()
    
    # --- Desenho do jogo AQUI
    
    # Limpar o ecrã (ecrã a preto)
    screen.fill(BLACK)
    
    # Desenhar todas as sprites de uma só vez.
    all_sprites_list.draw(screen)
 
    # Atualizar o ecrã com o que foi desenhado.
    pygame.display.flip()
     
    # --- Limitar a 60 frames por segundo
    clock.tick(60)
 
# Para o motor de jogo (após terminar o ciclo principal do programa)

pygame.quit()