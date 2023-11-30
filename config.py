#!/usr/bin/env python3
import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

SC_WIDTH = 1200
SC_HEIGHT = 700
BCKRND_COLOUR = (255, 154, 246)
PA1_COLOUR = (255, 154, 246)
PA2_COLOUR = (255, 255, 153)
BALL_COLOUR = (154, 195, 255)
FONT_MEDIUM = pygame.font.Font('freesansbold.ttf', 50)
FONT_SMALL = pygame.font.Font('freesansbold.ttf', 30)
BLIP = pygame.mixer.Sound('./sounds/blip.wav')
SCORE = pygame.mixer.Sound('./sounds/score.wav')
VICTORY = pygame.mixer.Sound('./sounds/victory.wav')
logo = pygame.image.load('./sprites/logo.png')
SMALLER_LOGO = pygame.transform.scale(logo, (330, 180))
