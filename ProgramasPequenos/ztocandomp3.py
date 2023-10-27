import pygame
import sys
def print_python_version():
    print(sys.version)
# pylint: disable=no-member
pygame.init()
pygame.mixer.music.load('once.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
