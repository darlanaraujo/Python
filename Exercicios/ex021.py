'''
DESAFIO 021

Faça um programa que ABRA E REPRODUZA UM AÚDIO DE UM ARQUIVO MP3.
'''
import pygame
pygame.mixer.init()
pygame.mixer.music.load('abertura.mp3')
pygame.mixer.music.play()

input('Agora você pode escutar? ')