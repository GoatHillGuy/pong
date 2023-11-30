#!/usr/bin/env python3
import pygame
import random
import config
import paddle
import ball
import powerups

# TODO
# Dont run code outside main function
# Make up/down method on the paddle class


pygame.init()
pygame.font.init()
pygame.mixer.init()
spawn = False
can_score1 = True
can_score2 = True
pfunc = 0
running = True
paused = False
powerups_enable = False

score1 = 0
score2 = 0
clock = pygame.time.Clock()
pspeed = 4

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
baxm = 3
baym = 3

puIx = 600
puIy = 350
puIw = 45
puIh = 45
puxm = 2
puym = 2

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((1200, 700))

# Set the caption of the screen
pygame.display.set_caption('Pong')

# Update the display using flip
pygame.display.flip()

text1 = config.FONT_MEDIUM.render(str(score1), True, (255, 154, 246))
textRect1 = text1.get_rect()
textRect1.center = (400, 50)

text2 = config.FONT_MEDIUM.render(str(score2), True, (255, 255, 253))
textRect2 = text2.get_rect()
textRect2.center = (800, 50)

textv1 = config.FONT_MEDIUM.render("Player 1 has won. Woohoo.", True, (0, 0, 0))
textRectv1 = textv1.get_rect()
textRectv1.center = (600, 350)

textv2 = config.FONT_MEDIUM.render("Player 2 has won. Yippee", True, (0, 0, 0))
textRectv2 = textv2.get_rect()
textRectv2.center = (600, 350)

textr = config.FONT_SMALL.render("Press X to replay", True, (0, 0, 0))
textRectr = textv2.get_rect()
textRectr.center = (600, 450)

textq = config.FONT_SMALL.render("Press Q to quit", True, (0, 0, 0))
textRectq = textv2.get_rect()
textRectq.center = (950, 450)


class Pause:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def pause(self):
        self.textp = config.FONT_MEDIUM.render("Paused", True, (0, 0, 0))
        self.textRectp = self.textp.get_rect()
        self.textRectp.center = (self.x1, self.y1)

        self.text_resume = config.FONT_SMALL.render("Press E to resume", True, (0, 0, 0))
        self.textRect_resume = self.text_resume.get_rect()
        self.textRect_resume.center = (self.x2, self.y2)

        screen.blit(config.SMALLER_LOGO, (440, 80))
        screen.blit(self.textp, self.textRectp)
        screen.blit(self.text_resume, self.textRect_resume)


pa1 = paddle.Paddle(p1x, p1y, p1w, p1h)
pa2 = paddle.Paddle(p2x, p2y, p2w, p2h)

# game loop
while running:
    # for loop through the event queue

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        pause = Pause(600, 350, 600, 450)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pa1.set_speed(pspeed)
            if event.key == pygame.K_w:
                pa1.set_speed(-pspeed)
            if event.key == pygame.K_k:
                pa2.set_speed(pspeed)
            if event.key == pygame.K_i:
                pa2.set_speed(-pspeed)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                pa1.set_speed(0)
            if event.key == pygame.K_w:
                pa1.set_speed(0)
            if event.key == pygame.K_k:
                pa2.set_speed(0)
            if event.key == pygame.K_i:
                pa2.set_speed(0)

    halfcourt = pygame.Rect(0, 0, 600, 700)
    screen.fill(config.BCKRND_COLOUR)
    pong_ball = ball.Ball(ballx, bally, ballw, ballh)
    if powerups_enable:
        pu_invincible = powerups.PU_invincible(puIx, puIy, puIw, puIh)
    pygame.draw.rect(screen, (255, 255, 153), halfcourt)
    pygame.draw.rect(screen, config.PA1_COLOUR, pa1.paddle())
    pygame.draw.rect(screen, config.PA2_COLOUR, pa2.paddle())
    pygame.draw.rect(screen, config.BALL_COLOUR, pong_ball.ball())

    text1 = config.FONT_MEDIUM.render(str(score1), True, (255, 154, 246))
    textRect1 = text1.get_rect()
    textRect1.center = (400, 50)

    text2 = config.FONT_MEDIUM.render(str(score2), True, (255, 255, 253))
    textRect2 = text2.get_rect()
    textRect2.center = (800, 50)

    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)

    prob = random.random()
    if prob < 0.01:
        spawn = True

    if powerups_enable:
        pygame.draw.rect(screen, config.BALL_COLOUR, pu_invincible.ball())

    if pa1.y <= 0:
        pa1.y = 0
    if pa1.y >= config.SC_HEIGHT - p1h:
        pa1.y = config.SC_HEIGHT - p1h
    if pa2.y <= 0:
        pa2.y = 0
    if pa2.y >= config.SC_HEIGHT - p2h:
        pa2.y = config.SC_HEIGHT - p2h

    if bally < ballh:
        # ball has hit the top
        baym *= -1
        pygame.mixer.Sound.play(config.BLIP)
    if bally > config.SC_HEIGHT - ballh:
        # ball has hit the bottom
        baym *= -1
        pygame.mixer.Sound.play(config.BLIP)

    if puIy < puIh:
        # ball has hit the top
        puym *= -1
        pygame.mixer.Sound.play(config.BLIP)
    if puIy > config.SC_HEIGHT - puIh:
        # ball has hit the bottom
        puym *= -1
        pygame.mixer.Sound.play(config.BLIP)

    if ballx == 0:
        ballx = 600
        bally = 350
        score2 += 1
        pygame.mixer.Sound.play(config.SCORE)
    if ballx > config.SC_WIDTH - ballw:
        ballx = 600
        bally = 350
        score1 += 1
        pygame.mixer.Sound.play(config.SCORE)

    k = pong_ball.ball()
    p1rect = pa1.paddle()
    p2rect = pa2.paddle()
    kpos = (k.x, k.y)
    if powerups_enable:
        pu1 = pu_invincible.ball()
        pu1pos = (pu1.x, pu1.y)

    collide1 = p1rect.collidepoint(kpos)
    collide2 = p2rect.collidepoint(kpos)

    if powerups_enable:
        pu1collide1 = p1rect.collidepoint(pu1pos)
        pu1collide2 = p2rect.collidepoint(pu1pos)

    if collide1:
        baxm *= -1
        pygame.mixer.Sound.play(config.BLIP)
    if collide2:
        baxm *= -1
        pygame.mixer.Sound.play(config.BLIP)

    if powerups_enable:
        if pu1collide1:
            puxm *= -1
            pygame.mixer.Sound.play(config.BLIP)
        if pu1collide2:
            puxm *= -1
            pygame.mixer.Sound.play(config.BLIP)

    if puIx < 0:
        if ballx > config.SC_WIDTH - ballw:
            baxm *= -1
    if puIx > config.SC_WIDTH - puIw:
        if ballx == 0:
            baxm *= -1

    ballx = ballx + baxm
    bally = bally + baym

    puIx = puIx + puxm
    puIy = puIy + puym

    if keys[pygame.K_ESCAPE]:
        pfunc
        paused = True

    if paused:
        pause.pause()
        baxm = 0
        baym = 0
        pa1.up_pressed = False
        pa1.down_pressed = False
        pa2.down_pressed = False
        pa2.up_pressed = False
        # pygame.display.update()
        if keys[pygame.K_e]:
            paused = False
            # pygame.display.update()
            baxm = 3
            baym = 3

    if score1 == 10:
        baxm = 0
        baym = 0
        pa1.acelleration = 0
        pa2.acelleration = 0
        screen.blit(textv1, textRectv1)
        screen.blit(textr, textRectr)
        screen.blit(textq, textRectq)
        screen.blit(config.SMALLER_LOGO, (440, 80))
        # pygame.mixer.Sound.play(victory)
        if keys[pygame.K_x]:
            score1 = 0
            score2 = 0
            baxm = 3
            baym = 3
            pa1.acelleration = 4
            pa2.acelleration = 4
        if keys[pygame.K_q]:
            running = False

    if score2 == 10:
        baxm = 0
        baym = 0
        pa1.acelleration = 0
        pa2.acelleration = 0
        screen.blit(textv2, textRectv2)
        screen.blit(textr, textRectr)
        screen.blit(textq, textRectq)
        screen.blit(config.SMALLER_LOGO, (440, 80))
        # pygame.mixer.Sound.play(victory)
        if keys[pygame.K_x]:
            score1 = 0
            score2 = 0
            baxm = 2
            baym = 0.75
            pa1.acelleration = 4
            pa2.acelleration = 4
        if keys[pygame.K_q]:
            running = False

    if powerups_enable is False:
        puIx = 600
        puIy = 350

    pa1.update()
    pa2.update()
    clock.tick(120)
    # Check for QUIT event
    pygame.display.update()
    if event.type == pygame.QUIT:
        running = False
