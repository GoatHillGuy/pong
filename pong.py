#!/usr/bin/env python3
import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()
# Define the background colour
# using RGB color coding.
SC_WIDTH = 1200
SC_HEIGHT = 700
PAUSED = False
PFUNC = 0
spawn = False

running = True

background_colour = (255, 154, 246)
paddle1_colour = (255, 154, 246)
paddle2_colour = (255, 255, 153)
ball_colour = (154, 195, 255)
score1 = 0
score2 = 0
clock = pygame.time.Clock()

pspeed = 20

p1x = 50
p1y = 100
p1w = 40
p1h = 125

p2x = 1100
p2y = 100
p2w = 40
p2h = 125

ballx = 600
bally = 350
ballw = 30
ballh = 30
BAXM = 3
BAYM = 3

pux = 600
puy = 350
puw = 45
puh = 45
PUXM = 2
PUYM = 2

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((1200, 700))

# Set the caption of the screen
pygame.display.set_caption('Pong')

# Update the display using flip
pygame.display.flip()

fontMedium = pygame.font.Font('freesansbold.ttf', 50)
fontSmall = pygame.font.Font('freesansbold.ttf', 30)
blip = pygame.mixer.Sound('./sounds/blip.wav')
score = pygame.mixer.Sound('./sounds/score.wav')
victory = pygame.mixer.Sound('./sounds/victory.wav')
logo = pygame.image.load('./sprites/logo.png')
smallerlogo = pygame.transform.scale(logo, (330, 180))

text1 = fontMedium.render(str(score1), True, (255, 154, 246))
textRect1 = text1.get_rect()
textRect1.center = (400, 50)

text2 = fontMedium.render(str(score2), True, (255, 255, 253))
textRect2 = text2.get_rect()
textRect2.center = (800, 50)

textv1 = fontMedium.render("Player 1 has won. Woohoo.", True, (0, 0, 0))
textRectv1 = textv1.get_rect()
textRectv1.center = (600, 350)

textv2 = fontMedium.render("Player 2 has won. Yippee", True, (0, 0, 0))
textRectv2 = textv2.get_rect()
textRectv2.center = (600, 350)

textr = fontSmall.render("Press X to replay", True, (0, 0, 0))
textRectr = textv2.get_rect()
textRectr.center = (600, 450)

textq = fontSmall.render("Press Q to quit", True, (0, 0, 0))
textRectq = textv2.get_rect()
textRectq.center = (950, 450)


class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velY = 0
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

    def paddle(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.velY = 0
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.y += self.velY
        if self.y >= SC_HEIGHT:
            self.y = SC_HEIGHT

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Ball:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def ball(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.speed = 10
        self.x += self.speed
        self.y += self.speed


class PU_invincible:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def ball(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.speed = 5
        self.x += self.speed
        self.y += self.speed


class Pause:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def pause(self):
        self.textp = fontMedium.render("Paused", True, (0, 0, 0))
        self.textRectp = self.textp.get_rect()
        self.textRectp.center = (self.x1, self.y1)

        self.text_resume = fontSmall.render("Press E to resume", True, (0, 0, 0))
        self.textRect_resume = self.text_resume.get_rect()
        self.textRect_resume.center = (self.x2, self.y2)

        screen.blit(smallerlogo, (440, 80))
        screen.blit(self.textp, self.textRectp)
        screen.blit(self.text_resume, self.textRect_resume)


pa1 = Paddle(p1x, p1y, p1w, p1h)
pa2 = Paddle(p2x, p2y, p2w, p2h)

# game loop
while running:
    # for loop through the event queue

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        pause = Pause(600, 350, 600, 450)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pa1.down_pressed = True
            if event.key == pygame.K_w:
                pa1.up_pressed = True
            if event.key == pygame.K_k:
                pa2.down_pressed = True
            if event.key == pygame.K_i:
                pa2.up_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                pa1.down_pressed = False
            if event.key == pygame.K_w:
                pa1.up_pressed = False
            if event.key == pygame.K_k:
                pa2.down_pressed = False
            if event.key == pygame.K_i:
                pa2.up_pressed = False

    halfcourt = pygame.Rect(0, 0, 600, 700)
    screen.fill(background_colour)
    ball = Ball(ballx, bally, ballw, ballh)
    pu_invincible = PU_invincible(pux, puy, puw, puh)
    pygame.draw.rect(screen, (255, 255, 153), halfcourt)
    pygame.draw.rect(screen, paddle1_colour, pa1.paddle())
    pygame.draw.rect(screen, paddle2_colour, pa2.paddle())
    pygame.draw.rect(screen, ball_colour, ball.ball())

    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)

    prob = random.random()
    if prob < 0.01:
        spawn = True

    if spawn:
        pygame.draw.rect(screen, ball_colour, pu_invincible.ball())

    if pa1.y <= 0:
        pa1.y = 0
    if pa1.y >= SC_HEIGHT - p1h:
        pa1.y = SC_HEIGHT - p1h
    if pa2.y <= 0:
        pa2.y = 0
    if pa2.y >= SC_HEIGHT - p2h:
        pa2.y = SC_HEIGHT - p2h

    if bally < ballh:
        # ball has hit the top
        BAYM *= -1
        pygame.mixer.Sound.play(blip)
    if bally > SC_HEIGHT - ballh:
        # ball has hit the bottom
        BAYM *= -1
        pygame.mixer.Sound.play(blip)

    if puy < puh:
        # ball has hit the top
        PUYM *= -1
        pygame.mixer.Sound.play(blip)
    if puy > SC_HEIGHT - puh:
        # ball has hit the bottom
        PUYM *= -1
        pygame.mixer.Sound.play(blip)

    # print(ballx)
    if ballx == 0:
        ballx = 600
        bally = 350
        score2 += 1
        pygame.mixer.Sound.play(score)
        pygame.display.update()
    if ballx > SC_WIDTH - ballw:
        ballx = 600
        bally = 350
        score1 += 1
        pygame.mixer.Sound.play(score)
        pygame.display.update()

    k = ball.ball()
    pu1 = pu_invincible.ball()
    p1rect = pa1.paddle()
    p2rect = pa2.paddle()
    kpos = (k.x, k.y)
    pu1pos = (pu1.x, pu1.y)

    collide1 = p1rect.collidepoint(kpos)
    collide2 = p2rect.collidepoint(kpos)

    pu1collide1 = p1rect.collidepoint(pu1pos)
    pu1collide2 = p2rect.collidepoint(pu1pos)

    if collide1:
        BAXM *= -1
        pygame.mixer.Sound.play(blip)
    if collide2:
        BAXM *= -1
        pygame.mixer.Sound.play(blip)

    if pu1collide1:
        PUXM *= -1
        pygame.mixer.Sound.play(blip)
    if pu1collide2:
        PUXM *= -1
        pygame.mixer.Sound.play(blip)

    ballx = ballx + BAXM
    bally = bally + BAYM

    pux = pux + PUXM
    puy = puy + PUYM

    if keys[pygame.K_ESCAPE]:
        PFUNC += 1
        PAUSED = True

    if PAUSED:
        pause.pause()
        BAXM = 0
        BAYM = 0
        pa1.up_pressed = False
        pa1.down_pressed = False
        pa2.down_pressed = False
        pa2.up_pressed = False
        # pygame.display.update()
        if keys[pygame.K_e]:
            PAUSED = False
            # pygame.display.update()
            BAXM = 3
            BAYM = 3

    if score1 == 10:
        BAXM = 0
        BAYM = 0
        pspeed = 0
        screen.blit(textv1, textRectv1)
        screen.blit(textr, textRectr)
        screen.blit(textq, textRectq)
        screen.blit(smallerlogo, (440, 80))
        # pygame.mixer.Sound.play(victory)
        if keys[pygame.K_x]:
            score1 = 0
            score2 = 0
            BAXM = 3
            BAYM = 3
            pspeed = 20
        if keys[pygame.K_q]:
            running = False

    if score2 == 10:
        BAXM = 0
        BAYM = 0
        pspeed = 0
        screen.blit(textv2, textRectv2)
        screen.blit(textr, textRectr)
        screen.blit(textq, textRectq)
        screen.blit(smallerlogo, (440, 80))
        # pygame.mixer.Sound.play(victory)
        if keys[pygame.K_x]:
            score1 = 0
            score2 = 0
            BAXM = 2
            BAYM = 0.75
            pspeed = 0
        if keys[pygame.K_q]:
            running = False

    pa1.update()
    pa2.update()
    clock.tick(120)
    # Check for QUIT event
    pygame.display.update()
    if event.type == pygame.QUIT:
        running = False
