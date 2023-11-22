#!/usr/bin/env python3
import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()
# Define the background colour
# using RGB color coding.
SC_WIDTH = 1200
SC_HEIGHT = 700
PAUSED = False
PFUNC = 0

background_colour = (255, 154, 246)
paddle1_colour = (255, 154, 246)
paddle2_colour = (255, 255, 153)
ball_colour = (154, 195, 255)
score1 = 0
score2 = 0

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
BAXM = 1
BAYM = 1

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


class Paddle1:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def paddle(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


# class Paddle2:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height

#     def paddle(self):
#         return pygame.Rect(self.x, self.y, self.width, self.height)


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


class Pause:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pause(self):
        textp = fontMedium.render("Paused", True, (0, 0, 0))
        textRectp = textp.get_rect()
        textRectp.center = (self.x, self.y)
        screen.blit(logo, (600, 250))
        screen.blit(textp, textRectp)


# Variable to keep our game loop running
running = True

# game loop
while running:
    # for loop through the event queue

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        pause = Pause(600, 350)
        if keys[pygame.K_s]:
            p1y += pspeed
        if keys[pygame.K_w]:
            p1y -= pspeed
        if keys[pygame.K_k]:
            p2y += pspeed
        if keys[pygame.K_i]:
            p2y -= pspeed
        # if keys[pygame.K_ESCAPE]:
        #     pause.pause()
        #     BAXM = 0
        #     BAYM = 0
        #     pygame.display.update()

    halfcourt = pygame.Rect(0, 0, 600, 700)
    screen.fill(background_colour)
    pa1 = Paddle1(p1x, p1y, p1w, p1h)
    pa2 = Paddle1(p2x, p2y, p2w, p2h)
    ball = Ball(ballx, bally, ballw, ballh)
    pygame.draw.rect(screen, (255, 255, 153), halfcourt)
    pygame.draw.rect(screen, paddle1_colour, pa1.paddle())
    pygame.draw.rect(screen, paddle2_colour, pa2.paddle())
    pygame.draw.rect(screen, ball_colour, ball.ball())

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

    textq = fontSmall.render("Press ESC to quit", True, (0, 0, 0))
    textRectq = textv2.get_rect()
    textRectq.center = (950, 450)

    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)

    if p1y <= 0:
        p1y = 0
    if p1y >= SC_HEIGHT - p1h:
        p1y = SC_HEIGHT - p1h
    if p2y <= 0:
        p2y = 0
    if p2y >= SC_HEIGHT - p2h:
        p2y = SC_HEIGHT - p2h

    if bally < ballh:
        # ball has hit the top
        BAYM *= -1
        pygame.mixer.Sound.play(blip)
    if bally > SC_HEIGHT - ballh:
        # ball has hit the bottom
        BAYM *= -1
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
    p1rect = pa1.paddle()
    p2rect = pa2.paddle()
    kpos = (k.x, k.y)

    collide1 = p1rect.collidepoint(kpos)
    collide2 = p2rect.collidepoint(kpos)

    if collide1:
        BAXM *= -1
        pygame.mixer.Sound.play(blip)
    if collide2:
        BAXM *= -1
        pygame.mixer.Sound.play(blip)

    ballx = ballx + BAXM
    bally = bally + BAYM

    if keys[pygame.K_ESCAPE]:
        PFUNC += 1
        PAUSED = True

    if PAUSED:
        pause.pause()
        BAXM = 0
        BAYM = 0
        pspeed = 0
        # pygame.display.update()
        if keys[pygame.K_e]:
            PAUSED = False
            # pygame.display.update()
            BAXM = 1
            BAYM = 1
            pspeed = 20

    if score1 == 10:
        BAXM = 0
        BAYM = 0
        pspeed = 0
        screen.blit(textv1, textRectv1)
        screen.blit(textr, textRectr)
        screen.blit(textq, textRectq)
        # pygame.mixer.Sound.play(victory)
        if keys[pygame.K_x]:
            score1 = 0
            score2 = 0
            BAXM = 1
            BAYM = 1
            pspeed = 20
        if keys[pygame.K_ESCAPE]:
            running = False

    if score2 == 10:
        BAXM = 0
        BAYM = 0
        pspeed = 0
        screen.blit(textv2, textRectv2)
        screen.blit(textr, textRectr)
        screen.blit(textq, textRectq)
        # pygame.mixer.Sound.play(victory)
        if keys[pygame.K_x]:
            score1 = 0
            score2 = 0
            BAXM = 1
            BAYM = 1
            pspeed = 0
        if keys[pygame.K_ESCAPE]:
            running = False

    if p1y >= SC_HEIGHT - p1h:
        p1y = SC_HEIGHT - p1h
    # Check for QUIT event
    pygame.display.update()
    if event.type == pygame.QUIT:
        running = False
