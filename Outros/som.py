'''import pygame

pygame.init()
pygame.mixer.music.load('frases.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

from pygame import mixer

mixer.init()
mixer.music.load('frases.mp3')
mixer.music.play()
input('Agora você pode escutar? ')