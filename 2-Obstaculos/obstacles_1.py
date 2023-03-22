import pygame
import random

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

# Define um tamanho (larguraxaltura) e cria a janela desse tamanho e com um titulo
janela_dimensao = (640, 480)
janela = pygame.display.set_mode(janela_dimensao)
pygame.display.set_caption("Fast'n Rocks")

# Cria os objetos de jogo
jog_largura = 50
jog_altura = 50
jog_x = janela_dimensao[0] // 2 - jog_largura // 2
jog_y = janela_dimensao[1] - jog_altura - 10

obstaculo_largura = 50
obstaculo_altura = 50
obstaculo_speed = 3
obstaculos = []

# Fonte a ser utilizada no jogo
font = pygame.font.Font(None, 30)

# Loop principal
pontuacao = 0
clock = pygame.time.Clock()
emJogo = True
while emJogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            emJogo = False
    
    # move o jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and jog_x > 0:
        jog_x -= 5
    elif keys[pygame.K_RIGHT] and jog_x < janela_dimensao[0] - jog_largura:
        jog_x += 5
  
    # move os obstaculos e cria novos
    for obstaculo in obstaculos:
        obstaculo[1] += obstaculo_speed
    # cria um obstaculo de 50 em 50 px
    if len(obstaculos) == 0 or obstaculos[-1][1] > 50:
        x = random.randint(0, janela_dimensao[0] - obstaculo_largura)
        obstaculos.append([x, -obstaculo_altura])
    # Se o obstaculo atingir o altura máxima do campo de jogo elimina-o do array
    if obstaculos[0][1] > janela_dimensao[1]:
        obstaculos.pop(0)

    # Verifica se houve colisão do jogador com um obstáculo
    for obstaculo in obstaculos:
        if jog_x < obstaculo[0] + obstaculo_largura and \
            jog_x + jog_largura > obstaculo[0] and \
            jog_y < obstaculo[1] + obstaculo_altura and \
            jog_y + jog_altura > obstaculo[1]:
            emJogo = False
    
    # Atualiza a pontuacao
    pontuacao += 1
    
    # Desenha o jogo
    janela.fill((0, 0, 0))
    for obstaculo in obstaculos:
        pygame.draw.rect(janela, RED, (obstaculo[0], obstaculo[1],\
        obstaculo_largura, obstaculo_altura))
    pygame.draw.rect(janela, BLUE, (jog_x, jog_y, jog_largura, jog_altura))
    score_text = font.render("Pontuação: " + str(pontuacao), True, WHITE)
    janela.blit(score_text, (janela_dimensao[0] // 2 - score_text.get_width() // 2, 20))

    # Atualiza o ecrã
    pygame.display.update()

    # Limita a fps a 60 ps
    clock.tick(60)

# Sai do jogo e escreve a pontuação final na linha de comando
pygame.quit()
print("Pontuação =",pontuacao)