import pygame as pg

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((1280, 720))

pos = pg.Vector2(600, 700)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            break

    pg.draw.polygon(surface=screen, color='red', points=pos, width=340)

    key = pg.key.get_pressed()
    if key == pg.K_a:
        pos.x -= 6
    if key == pg.K_d:
        pos.x += 6
    if key == pg.K_w:
        pos.y -= 6
    if key == pg.K_s:
        pos.y += 6
    elif key == pg.K_a and key == pg.K_LSHIFT:
        pos.x -= 60
    elif key == pg.K_d and key == pg.K_LSHIFT:
        pos.x += 60
    elif key == pg.K_w and key == pg.K_LSHIFT:
        pos.y -= 60
    elif key == pg.K_s and key == pg.K_LSHIFT:
        pos.y += 60

    pg.display.update()
    pg.display.flip()
    clock.tick(60)
