#!/usr/bin/env python3
import pygame
import config


class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0

    def paddle(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def set_speed(self, speed):
        self.speed = speed

    def update(self):
        self.y += self.speed
        if self.y >= config.SC_HEIGHT:
            self.y = config.SC_HEIGHT

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
