# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the drawing window
display_width = 700
display_height = 500
screen = pygame.display.set_mode([display_width, display_height])


# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a circle, rect, polygon and line
    pygame.draw.circle(screen, (0, 255, 0), (250, 250), 75)
    pygame.draw.rect(screen, (0, 0, 255), [100, 100, 100, 100])
    pygame.draw.polygon(screen, (0, 255, 255),
                        ((500, 50), (350, 200), (650, 200)))
    pygame.draw.line(screen, (0, 0, 0), (100, 50), (300, 50), 1)

    # get the mouse pos
    pos = pygame.mouse.get_pos()

    # show a text1 in corner of screen
    text1 = "hello!"
    font = pygame.font.SysFont(None, 25)
    text = font.render(text1 + str(pos), True, (255, 0, 0))
    screen.blit(text, (0, 0))

    # show a bog text2 in center of screen
    text2 = "goodby!"
    largeText = pygame.font.Font('freesansbold.ttf', 90)

    textSurface = largeText.render(text2, True, (0, 0, 0))
    TextSurf, TextRect = textSurface, textSurface.get_rect()

    TextRect.center = ((display_width/2), (display_height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
