#!/usr/bin/env python3
import pygame


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
