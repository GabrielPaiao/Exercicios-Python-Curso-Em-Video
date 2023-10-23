import pygame

pygame.init() #iniciar pygame
pygame.mixer.music.load('taylor.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
