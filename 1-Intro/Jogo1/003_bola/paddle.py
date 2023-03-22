import pygame
BLACK = (0,0,0)
 
class Paddle(pygame.sprite.Sprite):
    #Esta classe representa um paddle. Deriva da classe sprite do Pygame.
    
    def __init__(self, color, width, height):
        # CHama o construtor da classe (Sprite)
        super().__init__()
        
        # Definir a cor, largura e altura do paddle
        # Definir a cor do fundo e a sua transparencia.
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Desenhar o paddle ( que é um retangulo!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Obtém o objeto rectangulo que contém as medidas da imagem.
        self.rect = self.image.get_rect()
        

    # Mover paddle para a esquerda 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
		# Verificar se o paddle não sai pelo lado esquerdo do ecrã
        if self.rect.x < 0:
          self.rect.x = 0
    # Mover paddle para a direita          
    def moveRight(self, pixels):
        self.rect.x += pixels
	    # Verificar se o paddle não sai pelo lado direito do ecrã
        if self.rect.x > 650:
          self.rect.x = 650