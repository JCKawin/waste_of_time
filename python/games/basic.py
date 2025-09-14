import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pos = pygame.Vector2(640, 320)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')

    pygame.draw.circle(surface=screen, color="red", center=pos, radius=20)
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        pos.x += 2
    if key[pygame.K_a]:
        pos.x -= 2
    if key[pygame.K_w]:
        pos.y -= 2
    if key[pygame.K_s]:
        pos.y += 2
    if key[pygame.K_s] and key[pygame.K_LSHIFT]:
        pos.y += 20
    elif key[pygame.K_d] and key[pygame.K_LSHIFT]:
        pos.x += 20
    elif key[pygame.K_a] and key[pygame.K_LSHIFT]:
        pos.x -= 20
    elif key[pygame.K_w] and key[pygame.K_LSHIFT]:
        pos.y -= 20

    pygame.display.flip()

    clock.tick(60)
pygame.quit()
