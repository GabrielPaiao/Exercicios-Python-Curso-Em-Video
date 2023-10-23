"""Faça um programa que abra e reproduza um aúdio de um arquivo .mp3"""

import pygame

pygame.init() #iniciar pygame
pygame.mixer.music.load('taylor.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
