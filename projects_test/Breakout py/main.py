import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Configuración del bloque
block_width = 60
block_height = 20
blocks = [(x, y) for x in range(0, width, block_width) for y in range(0, 200, block_height)]

# Configuración de la barra y la pelota
bar_width, bar_height = 100, 10
bar = pygame.Rect(width // 2 - bar_width // 2, height - bar_height - 30, bar_width, bar_height)
ball = pygame.Rect(width // 2 - 10, height // 2 - 10, 20, 20)
ball_speed_x, ball_speed_y = 5, -5

# Configuración de la barra y la pelota
bar_speed = 10

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de la barra
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bar.x -= bar_speed
    if keys[pygame.K_RIGHT]:
        bar.x += bar_speed

    # Limitar la barra a la ventana
    if bar.x < 0:
        bar.x = 0
    if bar.x > width - bar_width:
        bar.x = width - bar_width

    # Movimiento de la pelota
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisiones con las paredes
    if ball.x <= 0 or ball.x >= width - ball.width:
        ball_speed_x *= -1
    if ball.y <= 0:
        ball_speed_y *= -1

    # Colisión con la barra
    if ball.colliderect(bar):
        ball_speed_y *= -1

    # Colisión con los bloques
    new_blocks = []
    for block in blocks:
        rect = pygame.Rect(block[0], block[1], block_width, block_height)
        if ball.colliderect(rect):
            ball_speed_y *= -1
        else:
            new_blocks.append(block)
    blocks = new_blocks

    # Dibujar todo
    screen.fill(black)
    pygame.draw.rect(screen, white, bar)
    pygame.draw.ellipse(screen, red, ball)
    for block in blocks:
        pygame.draw.rect(screen, red, pygame.Rect(block[0], block[1], block_width, block_height))
    
    pygame.display.flip()
    clock.tick(60)
