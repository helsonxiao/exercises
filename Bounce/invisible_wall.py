import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_item = pygame.image.load("doc1.gif")
x = 30
y = 30
x_speed = 5
y_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    pygame.time.delay(30)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 164, 134], 0)
    x = x + x_speed
    y = y + y_speed
    if x > 0.5 * screen.get_width() or x < 0:
        x_speed = -x_speed
    if y > 0.5 * screen.get_height() or y < 0:
        y_speed = -y_speed
    screen.blit(my_item, [x, y])
    pygame.display.flip()

pygame.quit()
