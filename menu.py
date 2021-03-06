# -*- coding: utf-8 -*-
import pygame
import sys


class Menu:
    def __init__(self):
        self.punkti = [[u'Го тестить!', (300, 270)], [u'Уйти', (340, 320)]]
        self.punkt = 0

    def render(self, screen):
        menu_font = pygame.font.Font(None, 50)
        for i in self.punkti:
            if self.punkti.index(i) == self.punkt:
                screen.blit(menu_font.render(i[0], 1, (255, 154, 43)), i[1])
            else:
                screen.blit(menu_font.render(i[0], 1, (200, 154, 43)), i[1])

    def menu(self, window):
        done = True
        pygame.font.init()
        screen = pygame.Surface((800, 630))
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if len(self.punkti)-1 != self.punkt:
                            self.punkt +=1
                        else:
                            self.punkt = 0
                    if event.key == pygame.K_UP:
                        if len(self.punkti) - 1 != self.punkt:
                            self.punkt += 1
                        else:
                            self.punkt = 0
                    if event.key == pygame.K_SPACE:
                        if self.punkt == 0:
                            done = False
                        else:
                            sys.exit()

            screen.fill((40, 110, 120))
            self.render(screen)
            window.blit(screen, (0, 0))

            pygame.display.flip()