# Importar a livraria pygame e inicializa o motor de jogo
import pygame

pygame.init()

# Definir cores
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Define um tamanho (larguraxaltura) e cria a janela desse tamanho e com um titulo
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Apanh'á Bola")
 
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

    # --- Lógica do jogo AQUI
 
    # --- Desenho do jogo AQUI
    
    # Limpar o ecrã (ecrã a preto)
    screen.fill(BLACK)
     
    # --- Limitar a 60 frames por segundo
    clock.tick(60)
 
# Para o motor de jogo (após terminar o ciclo principal do programa)

pygame.quit()