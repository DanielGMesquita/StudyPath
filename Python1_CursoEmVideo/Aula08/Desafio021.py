#Importar e tocar um arquivo mp3

import pygame
pygame.init()
pygame.mixer.music.load('ex01.mp3')
pygame.mixer.music.play()
pygame.event.wait()