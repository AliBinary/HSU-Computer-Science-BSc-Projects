# AliGhanbari
# 4001239216
import time
import pygame
pygame.init()
clock = pygame.time.Clock()

display_height = 600
display_width = 800
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('4001239216')

x, y = ((display_width/2), (display_height/2))

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
screen.fill(white)

pygame.draw.circle(screen, red, (x+100, y), 40)
pygame.draw.circle(screen, green, (x-36, y+84), 40)
pygame.draw.circle(screen, blue, (x-36, y-84), 40)
pygame.draw.line(screen, black, (x, y), (x+100, y), 5)
pygame.draw.line(screen, black, (x, y), (x-36, y+84), 5)
pygame.draw.line(screen, black, (x, y), (x-36, y-84), 5)

rotate = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if pygame.mouse.get_pressed()[0]:
        rotate = False
    if pygame.mouse.get_pressed()[2]:
        rotate = True

    if rotate:
        # screen.blit(pygame.transform.rotate(screen, 90), (x-190, y-190))
        pygame.transform.rotate(screen, 90)
        screen.get_rect(center = image.get_rect(topleft = topleft).center)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
