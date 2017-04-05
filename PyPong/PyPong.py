import pygame,sys, random
from pygame.locals import *


class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        global score, score_font, score_surf
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.left > screen.get_width() :
            self.speed[0] = -self.speed[0]
            if not done:
                hit_wall.play()
        if self.rect.top <= 0 :
            self.speed[1] = -self.speed[1]
            get_point.play()
            score = score + 1
            score_surf = score_font.render(str(score), 1, (0, 0, 0))


class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0, 0, 0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640, 480])
pygame.mixer.music.load("bg_music.mp3")
pygame.time.delay(1000)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.7)
hit_paddle = pygame.mixer.Sound("hit_paddle.wav")
hit_wall = pygame.mixer.Sound("hit_wall.wav")
new_life = pygame.mixer.Sound("new_life.wav")
game_over = pygame.mixer.Sound("game_over.wav")
get_point = pygame.mixer.Sound("get_point.wav")
splat = pygame.mixer.Sound("splat.wav")
hit_paddle.set_volume(0.5)
hit_wall.set_volume(0.5)
new_life.set_volume(0.5)
game_over.set_volume(1)
get_point.set_volume(0.5)
clock = pygame.time.Clock()
ball_speed = [10, 10]
myBall = MyBallClass("wackyball.bmp", ball_speed, [50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270,400])
score = 0
score_font = pygame.font.Font(None, 50)
score_surf = score_font.render(str(score), 1, (0, 0 ,0))
score_pos = [10, 10]
lives = 3
done = False
running = True
while running:
    clock.tick(30)
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myBall.speed[1] = -myBall.speed[1] - random.random()
        hit_paddle.play()

    myBall.move()

    if not done:
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_surf, score_pos)
        for i in range(lives):
            width = screen.get_width()
            screen.blit(myBall.image, [width - 40 * i, 20])
        pygame.display.flip()

    if myBall.rect.top >= screen.get_rect().bottom:
        lives = lives - 1
        if not done:
            splat.play()
        if lives <= 0:
            if not done:
                pygame.time.delay(1000)
                game_over.play()
            final_text1 = "Game Over"
            final_text2 = "Your final score is : " + str(score)
            ft1_font = pygame.font.Font(None , 50)
            ft1_surf = ft1_font.render(final_text1, 1, (0,0,0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = ft2_font.render(final_text2, 1, (0,0,0))
            screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 100])
            screen.blit(ft2_surf, [screen.get_width()/ 2 - ft2_surf.get_width() / 2, 200])
            pygame.display.flip()
            done = True
            pygame.mixer.music.fadeout(2000)
        else:  # wait 2 seconds, then start the next ball
            pygame.time.delay(1000)
            new_life.play()
            pygame.time.delay(1000)
            myBall.rect.topleft = [(screen.get_rect().width) - 40 * lives, 20]
pygame.quit()