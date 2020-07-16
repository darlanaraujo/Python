'''
DESAFIO 021

Faça um programa que ABRA E REPRODUZA UM AÚDIO DE UM ARQUIVO MP3.
'''
import pygame
pygame.init()
pygame.mixer.music.load('abertura.mp3')
pygame.mixer.music.play()
pygame.event.wait()